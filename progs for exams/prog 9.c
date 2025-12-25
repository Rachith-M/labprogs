#include <stdio.h>
#include <stdlib.h>

/* Node definition */
typedef struct Node {
    int data;
    struct Node *next;
} Node;

/* Stack functions */
void push(Node **top, int val);
void pop(Node **top);
void displayStack(Node *top);

/* Queue functions */
void enqueue(Node **front, Node **rear, int val);
void dequeue(Node **front, Node **rear);
void displayQueue(Node *front);

int main() {
    Node *top = NULL;           // Stack
    Node *front = NULL, *rear = NULL; // Queue
    int choice, val;

    while (1) {
        printf("\n1.Push(Stack)\n2.Pop(Stack)\n3.Display Stack");
        printf("\n4.Enqueue(Queue)\n5.Dequeue(Queue)\n6.Display Queue\n7.Exit\n");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter value: ");
                scanf("%d", &val);
                push(&top, val);
                break;

            case 2:
                pop(&top);
                break;

            case 3:
                displayStack(top);
                break;

            case 4:
                printf("Enter value: ");
                scanf("%d", &val);
                enqueue(&front, &rear, val);
                break;

            case 5:
                dequeue(&front, &rear);
                break;

            case 6:
                displayQueue(front);
                break;

            case 7:
                exit(0);

            default:
                printf("Invalid choice!\n");
        }
    }
    return 0;
}

/* -------- STACK IMPLEMENTATION -------- */

void push(Node **top, int val) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = val;
    newNode->next = *top;
    *top = newNode;
    printf("%d pushed to stack\n", val);
}

void pop(Node **top) {
    if (*top == NULL) {
        printf("Stack is empty!\n");
        return;
    }
    Node *temp = *top;
    printf("%d popped from stack\n", temp->data);
    *top = temp->next;
    free(temp);
}

void displayStack(Node *top) {
    if (top == NULL) {
        printf("Stack is empty!\n");
        return;
    }
    printf("Stack:\n");
    while (top != NULL) {
        printf("%d -> ", top->data);
        top = top->next;
    }
    printf("NULL\n");
}

/* -------- QUEUE IMPLEMENTATION -------- */

void enqueue(Node **front, Node **rear, int val) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = val;
    newNode->next = NULL;

    if (*rear == NULL) {
        *front = *rear = newNode;
    } else {
        (*rear)->next = newNode;
        *rear = newNode;
    }
    printf("%d enqueued to queue\n", val);
}

void dequeue(Node **front, Node **rear) {
    if (*front == NULL) {
        printf("Queue is empty!\n");
        return;
    }
    Node *temp = *front;
    printf("%d dequeued from queue\n", temp->data);
    *front = temp->next;

    if (*front == NULL)
        *rear = NULL;

    free(temp);
}

void displayQueue(Node *front) {
    if (front == NULL) {
        printf("Queue is empty!\n");
        return;
    }
    printf("Queue:\n");
    while (front != NULL) {
        printf("%d -> ", front->data);
        front = front->next;
    }
    printf("NULL\n");
}
