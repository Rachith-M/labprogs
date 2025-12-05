#include <stdio.h>
#include <stdlib.h>

#define SIZE 10

int deque[SIZE];
int front = -1, rear = -1;

// ----- Utility functions -----
int isEmpty() {
    return (front == -1);
}

int isFull() {
    return ((rear + 1) % SIZE == front);
}

// ----- Insert Left -----
void insert_left(int val) {
    if (isFull()) {
        printf("Deque is FULL!\n");
        return;
    }

    if (isEmpty()) {
        front = rear = 0;
    } else {
        front = (front - 1 + SIZE) % SIZE;   // wrap-around backward
    }

    deque[front] = val;
}

// ----- Insert Right -----
void insert_right(int val) {
    if (isFull()) {
        printf("Deque is FULL!\n");
        return;
    }

    if (isEmpty()) {
        front = rear = 0;
    } else {
        rear = (rear + 1) % SIZE;   // wrap-around forward
    }

    deque[rear] = val;
}

// ----- Delete Left -----
void delete_left() {
    if (isEmpty()) {
        printf("Deque is EMPTY!\n");
        return;
    }

    printf("Deleted %d\n", deque[front]);

    if (front == rear) {  
        front = rear = -1;   // deque becomes empty
    } else {
        front = (front + 1) % SIZE;
    }
}

// ----- Delete Right -----
void delete_right() {
    if (isEmpty()) {
        printf("Deque is EMPTY!\n");
        return;
    }

    printf("Deleted %d\n", deque[rear]);

    if (front == rear) {
        front = rear = -1;
    } else {
        rear = (rear - 1 + SIZE) % SIZE;  // wrap-around backward
    }
}

// ----- Display -----
void display() {
    if (isEmpty()) {
        printf("Deque is EMPTY!\n");
        return;
    }

    printf("Deque elements: ");
    int i = front;

    while (1) {
        printf("%d ", deque[i]);
        if (i == rear)
            break;
        i = (i + 1) % SIZE;
    }
    printf("\n");
}

// ----- Main -----
int main() {
    int choice, val;

    while (1) {
        printf("\n---- DEQUE MENU ----\n");
        printf("1. Insert Left\n");
        printf("2. Insert Right\n");
        printf("3. Delete Left\n");
        printf("4. Delete Right\n");
        printf("5. Display\n");
        printf("6. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter value: ");
                scanf("%d", &val);
                insert_left(val);
                break;

            case 2:
                printf("Enter value: ");
                scanf("%d", &val);
                insert_right(val);
                break;

            case 3:
                delete_left();
                break;

            case 4:
                delete_right();
                break;

            case 5:
                display();
                break;

            case 6:
                exit(0);

            default:
                printf("Invalid choice!\n");
        }
    }
    return 0;
}
