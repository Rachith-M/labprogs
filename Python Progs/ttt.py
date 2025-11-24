import math

PLAYER = -1
AI = 1
EMPTY = 0

initial_board = [
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]

def is_board_full(board):
    return all(cell != EMPTY for row in board for cell in row)

def has_won(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

def evaluate(board):
    if has_won(board, AI):
        return 1
    elif has_won(board, PLAYER):
        return -1
    else:
        return 0

def minimax(board, alpha, beta, current_player):
    score = evaluate(board)
    if score == 1:
        return score
    if score == -1:
        return score
    if is_board_full(board):
        return 0

    empty_cells = get_empty_cells(board)

    if current_player == AI:
        max_eval = -math.inf
        for (i, j) in empty_cells:
            board[i][j] = AI
            eval_value = minimax(board, alpha, beta, PLAYER)
            board[i][j] = EMPTY
            max_eval = max(max_eval, eval_value)
            alpha = max(alpha, eval_value)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for (i, j) in empty_cells:
            board[i][j] = PLAYER
            eval_value = minimax(board, alpha, beta, AI)
            board[i][j] = EMPTY
            min_eval = min(min_eval, eval_value)
            beta = min(beta, eval_value)
            if beta <= alpha:
                break
        return min_eval

def find_best_move(board):
    best_eval = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                eval_value = minimax(board, -math.inf, math.inf, PLAYER)
                board[i][j] = EMPTY
                if eval_value > best_eval:
                    best_eval = eval_value
                    best_move = (i, j)
    return best_move

def print_board(board):
    for row in board:
        print(" ".join(["X" if cell == AI else "O" if cell == PLAYER else "-" for cell in row]))
    print()

def play_game():
    board = [row[:] for row in initial_board]
    print("Welcome to Tic Tac Toe (AI uses Alpha-Beta Pruning)!")
    print("You are 'O'. AI is 'X'.")
    print_board(board)

    while True:
        if has_won(board, AI):
            print("AI wins! Better luck next time!")
            break
        if has_won(board, PLAYER):
            print("Congratulations! You win!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

        try:
            row, col = map(int, input("Enter your move (row and column 0-2, space separated): ").split())
            if(0<=row<=2 and 0<=col<=2):
                pass
            else:
                raise ValueError
            
        except ValueError:
            print("Invalid input. Please enter two numbers between 0 and 2.")
            continue

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Invalid position. Please enter values between 0 and 2.")
            continue

        if board[row][col] != EMPTY:
            print("Cell already occupied. Try again.")
            continue

        board[row][col] = PLAYER
        print("Your move:")
        print_board(board)

        if has_won(board, PLAYER):
            print("Congratulations! You win!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

        print("AI is thinking...")
        ai_move = find_best_move(board)
        if ai_move is not None:
            ai_row, ai_col = ai_move
            board[ai_row][ai_col] = AI
            print("AI's move:")
            print_board(board)
        else:
            print("It's a draw!")
            break

        if has_won(board, AI):
            print("AI wins! Better luck next time!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
