import tkinter as tk
from tkinter import font as tkfont
import threading
import base64
import json
import urllib.request
import urllib.error
import mss
import mss.tools
from PIL import Image
import io
import time
from pynput import keyboard

# ── CONFIG ────────────────────────────────────────────────────────────────────
HOTKEY        = {keyboard.Key.ctrl, keyboard.Key.shift, keyboard.KeyCode.from_char('h')}
API_KEY_FILE  = "api_key.txt"
MODEL         = "meta-llama/llama-4-scout-17b-16e-instruct"
MAX_TOKENS    = 1024
GROQ_API_URL  = "https://api.groq.com/openai/v1/chat/completions"

SYSTEM_PROMPT = """You are a sharp, fast exam assistant. The user has shared their screen showing a question or problem.

Your job:
1. Identify the question on screen
2. Give the correct answer immediately — direct and confident
3. Add a one-line explanation if it helps clarity
4. Keep it SHORT. No fluff, no disclaimers.

Format:
ANSWER: <the answer>
WHY: <one-line reason> (skip if obvious)"""

# ── COLORS ────────────────────────────────────────────────────────────────────
BG          = "#0d0d0f"
BG_CARD     = "#13131a"
BORDER      = "#2a2a3d"
ACCENT      = "#7c6af7"
ACCENT2     = "#a78bfa"
TEXT        = "#e8e6f0"
TEXT_DIM    = "#6b6880"
TEXT_ANSWER = "#c4b5fd"
GREEN       = "#34d399"
RED         = "#f87171"
AMBER       = "#fbbf24"


def load_api_key():
    try:
        with open(API_KEY_FILE) as f:
            return f.read().strip()
    except FileNotFoundError:
        return None


def capture_screen():
    with mss.mss() as sct:
        monitor = sct.monitors[0]
        shot = sct.grab(monitor)
        img = Image.frombytes("RGB", shot.size, shot.bgra, "raw", "BGRX")
        w, h = img.size
        scale = min(1.0, 1280 / w)
        img = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=75)
        return base64.standard_b64encode(buf.getvalue()).decode()


def ask_groq(api_key, image_b64, extra_question=""):
    user_content = [
        {"type": "text", "text": extra_question if extra_question else "What is the question on screen? Answer it."},
        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_b64}"}}
    ]

    payload = json.dumps({
        "model": MODEL,
        "max_completion_tokens": MAX_TOKENS,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_content}
        ]
    }).encode()

    req = urllib.request.Request(
        GROQ_API_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        },
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())
        return data["choices"][0]["message"]["content"]


# ── OVERLAY WINDOW ────────────────────────────────────────────────────────────
class ScreenAssistant:
    def __init__(self):
        self.api_key = load_api_key()
        self.pressed_keys = set()
        self.is_capturing = False
        self.is_minimized = False
        self._saved_geometry = None
        self._saved_width = 360

        self.root = tk.Tk()
        self.root.title("")
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.attributes("-alpha", 0.97)
        self.root.configure(bg=BG)

        self._build_ui()
        self._position_window()
        self._start_hotkey_listener()

        self._drag_x = 0
        self._drag_y = 0
        self.header.bind("<ButtonPress-1>", self._drag_start)
        self.header.bind("<B1-Motion>", self._drag_move)
        self.title_label.bind("<ButtonPress-1>", self._drag_start)
        self.title_label.bind("<B1-Motion>", self._drag_move)
        # double-click header to restore
        self.header.bind("<Double-Button-1>", lambda e: self._restore_if_minimized())
        self.title_label.bind("<Double-Button-1>", lambda e: self._restore_if_minimized())

    # ── UI BUILD ──────────────────────────────────────────────────────────────
    def _build_ui(self):
        W = 360

        outer = tk.Frame(self.root, bg=ACCENT, padx=1, pady=1)
        outer.pack(fill="both", expand=True)

        self.inner = tk.Frame(outer, bg=BG)
        self.inner.pack(fill="both", expand=True)

        # HEADER
        self.header = tk.Frame(self.inner, bg=BG_CARD, height=38)
        self.header.pack(fill="x")
        self.header.pack_propagate(False)

        dots_frame = tk.Frame(self.header, bg=BG_CARD)
        dots_frame.pack(side="left", padx=10)
        for c in [RED, AMBER, GREEN]:
            tk.Label(dots_frame, text="●", fg=c, bg=BG_CARD,
                     font=("Courier", 7)).pack(side="left", padx=1)

        self.title_label = tk.Label(self.header, text="⚡ SCREEN AI  ·  GROQ",
                                    fg=ACCENT2, bg=BG_CARD,
                                    font=("Courier New", 10, "bold"))
        self.title_label.pack(side="left", padx=6)

        self.status_dot = tk.Label(self.header, text="●", fg=TEXT_DIM,
                                   bg=BG_CARD, font=("Courier", 9))
        self.status_dot.pack(side="right", padx=4)

        self.status_label = tk.Label(self.header, text="READY",
                                     fg=TEXT_DIM, bg=BG_CARD,
                                     font=("Courier New", 7, "bold"))
        self.status_label.pack(side="right", padx=2)

        close_btn = tk.Label(self.header, text="✕", fg=TEXT_DIM, bg=BG_CARD,
                             font=("Courier New", 11), cursor="hand2")
        close_btn.pack(side="right", padx=10)
        close_btn.bind("<Button-1>", lambda e: self.root.destroy())
        close_btn.bind("<Enter>", lambda e: close_btn.config(fg=RED))
        close_btn.bind("<Leave>", lambda e: close_btn.config(fg=TEXT_DIM))

        # BODY — pack_forget this to minimize
        self.body_frame = tk.Frame(self.inner, bg=BG)
        self.body_frame.pack(fill="both", expand=True)

        tk.Frame(self.body_frame, bg=BORDER, height=1).pack(fill="x")

        # API KEY
        key_frame = tk.Frame(self.body_frame, bg=BG, padx=12, pady=8)
        key_frame.pack(fill="x")

        tk.Label(key_frame, text="GROQ API KEY", fg=TEXT_DIM,
                 bg=BG, font=("Courier New", 7, "bold")).pack(anchor="w")

        key_row = tk.Frame(key_frame, bg=BG)
        key_row.pack(fill="x", pady=(3, 0))

        self.key_entry = tk.Entry(key_row, bg=BG_CARD, fg=TEXT, insertbackground=ACCENT2,
                                  relief="flat", font=("Courier New", 9), show="●",
                                  highlightthickness=1, highlightbackground=BORDER,
                                  highlightcolor=ACCENT)
        self.key_entry.pack(side="left", fill="x", expand=True, ipady=5, padx=(0, 6))
        if self.api_key:
            self.key_entry.insert(0, self.api_key)

        save_btn = tk.Label(key_row, text="SAVE", fg=BG, bg=ACCENT,
                            font=("Courier New", 8, "bold"), cursor="hand2",
                            padx=8, pady=4)
        save_btn.pack(side="right")
        save_btn.bind("<Button-1>", self._save_key)

        tk.Frame(self.body_frame, bg=BORDER, height=1).pack(fill="x")

        # HOTKEY HINT
        hint_frame = tk.Frame(self.body_frame, bg=BG, padx=12, pady=6)
        hint_frame.pack(fill="x")
        tk.Label(hint_frame, text="CAPTURE HOTKEY", fg=TEXT_DIM, bg=BG,
                 font=("Courier New", 7, "bold")).pack(side="left")
        tk.Label(hint_frame, text="Ctrl + Shift + H", fg=ACCENT2, bg=BG,
                 font=("Courier New", 8, "bold")).pack(side="right")

        tk.Frame(self.body_frame, bg=BORDER, height=1).pack(fill="x")

        # ANSWER AREA
        answer_container = tk.Frame(self.body_frame, bg=BG, padx=12, pady=10)
        answer_container.pack(fill="both", expand=True)

        header_row = tk.Frame(answer_container, bg=BG)
        header_row.pack(fill="x", pady=(0, 6))
        tk.Label(header_row, text="ANSWER", fg=TEXT_DIM, bg=BG,
                 font=("Courier New", 7, "bold")).pack(side="left")

        self.copy_btn = tk.Label(header_row, text="COPY", fg=TEXT_DIM, bg=BG,
                                 font=("Courier New", 7, "bold"), cursor="hand2")
        self.copy_btn.pack(side="right")
        self.copy_btn.bind("<Button-1>", self._copy_answer)
        self.copy_btn.bind("<Enter>", lambda e: self.copy_btn.config(fg=ACCENT2))
        self.copy_btn.bind("<Leave>", lambda e: self.copy_btn.config(fg=TEXT_DIM))

        txt_frame = tk.Frame(answer_container, bg=BG_CARD,
                             highlightthickness=1, highlightbackground=BORDER)
        txt_frame.pack(fill="both", expand=True)

        scrollbar = tk.Scrollbar(txt_frame, bg=BG_CARD, troughcolor=BG,
                                 highlightthickness=0, bd=0, width=6)
        scrollbar.pack(side="right", fill="y")

        self.answer_text = tk.Text(txt_frame, bg=BG_CARD, fg=TEXT_ANSWER,
                                   font=("Courier New", 9), wrap="word",
                                   relief="flat", bd=0, padx=10, pady=10,
                                   height=10, width=W // 9,
                                   yscrollcommand=scrollbar.set,
                                   cursor="arrow", state="disabled",
                                   insertbackground=ACCENT2,
                                   selectbackground=ACCENT,
                                   selectforeground=TEXT)
        self.answer_text.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.answer_text.yview)

        self.answer_text.tag_configure("placeholder", foreground=TEXT_DIM,
                                       font=("Courier New", 8))
        self.answer_text.tag_configure("answer", foreground=TEXT_ANSWER,
                                       font=("Courier New", 9))
        self.answer_text.tag_configure("bold", foreground=GREEN,
                                       font=("Courier New", 9, "bold"))
        self.answer_text.tag_configure("error", foreground=RED,
                                       font=("Courier New", 9))

        self._set_placeholder()

        # CAPTURE BUTTON
        tk.Frame(self.body_frame, bg=BORDER, height=1).pack(fill="x")

        btn_frame = tk.Frame(self.body_frame, bg=BG, padx=12, pady=10)
        btn_frame.pack(fill="x")

        self.capture_btn = tk.Label(btn_frame, text="⚡  CAPTURE SCREEN",
                                    fg=BG, bg=ACCENT,
                                    font=("Courier New", 9, "bold"),
                                    cursor="hand2", pady=7, padx=12)
        self.capture_btn.pack(fill="x")
        self.capture_btn.bind("<Button-1>", lambda e: self._trigger_capture())
        self.capture_btn.bind("<Enter>", lambda e: self.capture_btn.config(bg=ACCENT2))
        self.capture_btn.bind("<Leave>", lambda e: self.capture_btn.config(bg=ACCENT))

        self.min_btn = tk.Label(btn_frame, text="— minimize", fg=TEXT_DIM, bg=BG,
                                font=("Courier New", 7), cursor="hand2")
        self.min_btn.pack(pady=(6, 0))
        self.min_btn.bind("<Button-1>", lambda e: self._toggle_minimize())

    # ── HELPERS ───────────────────────────────────────────────────────────────
    def _position_window(self):
        self.root.update_idletasks()
        sw = self.root.winfo_screenwidth()
        w = self.root.winfo_width()
        self.root.geometry(f"+{sw - w - 20}+40")

    def _set_placeholder(self):
        self.answer_text.config(state="normal")
        self.answer_text.delete("1.0", "end")
        self.answer_text.insert("1.0",
            "Press  Ctrl+Shift+H  or click CAPTURE\nto analyze what's on screen.",
            "placeholder")
        self.answer_text.config(state="disabled")

    def _set_answer(self, text, is_error=False):
        self.answer_text.config(state="normal")
        self.answer_text.delete("1.0", "end")
        tag = "error" if is_error else "answer"
        lines = text.split("\n")
        for line in lines:
            if line.startswith("ANSWER:"):
                self.answer_text.insert("end", "ANSWER:", "bold")
                self.answer_text.insert("end", line[7:] + "\n", "answer")
            elif line.startswith("WHY:"):
                self.answer_text.insert("end", "WHY:", "bold")
                self.answer_text.insert("end", line[4:] + "\n", "answer")
            else:
                self.answer_text.insert("end", line + "\n", tag)
        self.answer_text.config(state="disabled")
        self.answer_text.see("1.0")

    def _set_status(self, label, color):
        self.status_label.config(text=label, fg=color)
        self.status_dot.config(fg=color)

    def _save_key(self, event=None):
        key = self.key_entry.get().strip()
        if key:
            self.api_key = key
            with open(API_KEY_FILE, "w") as f:
                f.write(key)
            self._set_status("KEY SAVED", GREEN)
            self.root.after(2000, lambda: self._set_status("READY", TEXT_DIM))

    def _copy_answer(self, event=None):
        txt = self.answer_text.get("1.0", "end").strip()
        if txt:
            self.root.clipboard_clear()
            self.root.clipboard_append(txt)
            self.copy_btn.config(text="COPIED!", fg=GREEN)
            self.root.after(1500, lambda: self.copy_btn.config(text="COPY", fg=TEXT_DIM))

    def _toggle_minimize(self):
        if not self.is_minimized:
            self.root.update_idletasks()
            x = self.root.winfo_x()
            y = self.root.winfo_y()
            w = self.root.winfo_width()
            self._saved_geometry = f"+{x}+{y}"
            self._saved_width = w
            # Hide body then lock to header height
            self.body_frame.pack_forget()
            self.root.geometry(f"{w}x40+{x}+{y}")
            self.is_minimized = True
            self.min_btn.config(text="▲ restore")
        else:
            self._do_restore()

    def _restore_if_minimized(self):
        if self.is_minimized:
            self._do_restore()

    def _do_restore(self):
        # Re-attach body, then restore saved position
        self.body_frame.pack(fill="both", expand=True)
        self.root.update_idletasks()
        if self._saved_geometry:
            # Let geometry be natural height but keep saved x/y
            w = self._saved_width
            geo = f"{w}x600{self._saved_geometry}"
            self.root.geometry(geo)
            # After layout settles, let it shrink to fit
            self.root.after(10, lambda: self.root.geometry(
                f"{w}x{self.root.winfo_reqheight()}{self._saved_geometry}"
            ))
        else:
            self._position_window()
        self.is_minimized = False
        self.min_btn.config(text="— minimize")

    # ── DRAG ──────────────────────────────────────────────────────────────────
    def _drag_start(self, event):
        self._drag_x = event.x_root - self.root.winfo_x()
        self._drag_y = event.y_root - self.root.winfo_y()

    def _drag_move(self, event):
        x = event.x_root - self._drag_x
        y = event.y_root - self._drag_y
        self.root.geometry(f"+{x}+{y}")

    # ── HOTKEY LISTENER ───────────────────────────────────────────────────────
    def _normalize_key(self, key):
        # Windows sends ctrl_l/ctrl_r instead of Key.ctrl — normalize all variants
        _map = {
            keyboard.Key.ctrl_l:  keyboard.Key.ctrl,
            keyboard.Key.ctrl_r:  keyboard.Key.ctrl,
            keyboard.Key.shift_l: keyboard.Key.shift,
            keyboard.Key.shift_r: keyboard.Key.shift,
            keyboard.Key.alt_l:   keyboard.Key.alt,
            keyboard.Key.alt_r:   keyboard.Key.alt,
            keyboard.Key.alt_gr:  keyboard.Key.alt,
        }
        return _map.get(key, key)

    def _start_hotkey_listener(self):
        H_VK = 72  # Virtual key code for H — always 72 regardless of Ctrl/Shift state

        def _is_h(key):
            return isinstance(key, keyboard.KeyCode) and key.vk == H_VK

        def on_press(key):
            nkey = self._normalize_key(key)
            self.pressed_keys.add(nkey)

            ctrl_held  = keyboard.Key.ctrl  in self.pressed_keys
            shift_held = keyboard.Key.shift in self.pressed_keys
            h_held     = _is_h(key)

            if ctrl_held and shift_held and h_held:
                if not self.is_capturing:
                    self.pressed_keys.clear()
                    self.root.after(0, self._trigger_capture)

        def on_release(key):
            nkey = self._normalize_key(key)
            self.pressed_keys.discard(nkey)

        listener = keyboard.Listener(on_press=on_press, on_release=on_release)
        listener.daemon = True
        listener.start()

    # ── CAPTURE & QUERY ───────────────────────────────────────────────────────
    def _trigger_capture(self):
        if self.is_capturing:
            return
        if not self.api_key:
            self._set_answer("⚠ Please enter your Groq API key first.", is_error=True)
            return

        self.is_capturing = True
        self.capture_btn.config(text="⏳  CAPTURING...", bg="#3d3560", fg=TEXT_DIM)
        self._set_status("CAPTURING", AMBER)
        self.answer_text.config(state="normal")
        self.answer_text.delete("1.0", "end")
        self.answer_text.insert("1.0", "Capturing screen...", "placeholder")
        self.answer_text.config(state="disabled")

        threading.Thread(target=self._capture_thread, daemon=True).start()

    def _capture_thread(self):
        try:
            self.root.after(0, lambda: self._set_status("ANALYZING", ACCENT))
            self.root.after(0, lambda: self._update_answer_text("Sending to Groq...", "placeholder"))

            image_b64 = capture_screen()
            answer = ask_groq(self.api_key, image_b64)

            self.root.after(0, lambda: self._set_answer(answer))
            self.root.after(0, lambda: self._set_status("DONE", GREEN))
            self.root.after(0, lambda: self.root.after(3000, lambda: self._set_status("READY", TEXT_DIM)))

        except urllib.error.HTTPError as e:
            body = e.read().decode()
            self.root.after(0, lambda: self._set_answer(f"API Error {e.code}: {body}", is_error=True))
            self.root.after(0, lambda: self._set_status("ERROR", RED))
        except Exception as e:
            self.root.after(0, lambda: self._set_answer(f"Error: {str(e)}", is_error=True))
            self.root.after(0, lambda: self._set_status("ERROR", RED))
        finally:
            self.is_capturing = False
            self.root.after(0, lambda: self.capture_btn.config(
                text="⚡  CAPTURE SCREEN", bg=ACCENT, fg=BG))

    def _update_answer_text(self, text, tag):
        self.answer_text.config(state="normal")
        self.answer_text.delete("1.0", "end")
        self.answer_text.insert("1.0", text, tag)
        self.answer_text.config(state="disabled")

    # ── RUN ───────────────────────────────────────────────────────────────────
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = ScreenAssistant()
    app.run()