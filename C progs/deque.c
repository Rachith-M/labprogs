#include <stdio.h>
#include <stdlib.h>

#define SIZE 10
int queue[SIZE];
int right = -1, left = -1;

void enqueue_right(int);
void enqueue_left(int);
int dequeue_right();
int dequeue_left();
void display();

void main() {
    int choice, val;
    while (1) {
        printf("\nEnter your choice:\n");
        printf("1.Insert at right\n2.Insert at left\n3.Delete at right\n4.Delete at left\n5.Display\n6.Exit\n");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                printf("Enter the value to be inserted at right: ");
                scanf("%d", &val);
                enqueue_right(val);
                break;
            case 2:
                printf("Enter the value to be inserted at left: ");
                scanf("%d", &val);
                enqueue_left(val);
                break;
            case 3:
                dequeue_right();
                break;
            case 4:
                dequeue_left();
                break;
            case 5:
                display();
                break;
            case 6:
                exit(0);
            default:
                printf("Invalid input! Please try again!\n");
        }
    }
}

void enqueue_right(int value) {
    if ((left == 0 && right == SIZE - 1) || (left == right + 1)) {
        printf("Queue is full!\n");
        return;
    }
    if (left == -1) {
        left = right = 0;
    } else if (right == SIZE - 1) {
        right = 0;
    } else {
        right++;
    }
    queue[right] = value;
}

void enqueue_left(int value) {
    if ((left == 0 && right == SIZE - 1) || (left == right + 1)) {
        printf("Queue is full!\n");
        return;
    }
    if (left == -1) {
        left = right = 0;
    } else if (left == 0) {
        left = SIZE - 1;
    } else {
        left--;
    }
    queue[left] = value;
}

int dequeue_right() {
    if (left == -1) {
        printf("Underflow!\n");
        return -1;
    }
    printf("The deleted element is: %d\n", queue[right]);
    if (left == right) {
        left = right = -1;
    } else if (right == 0) {
        right = SIZE - 1;
    } else {
        right--;
    }
    return 0;
}

int dequeue_left() {
    if (left == -1) {
        printf("Underflow!\n");
        return -1;
    }
    printf("The deleted element is: %d\n", queue[left]);
    if (left == right) {
        left = right = -1;
    } else if (left == SIZE - 1) {
        left = 0;
    } else {
        left++;
    }
    return 0;
}

void display() {
    if (left == -1) {
        printf("Queue is empty!\n");
        return;
    }
    printf("The elements of the queue are:\n");
    int i = left;
    while (1) {
        printf("%d\t", queue[i]);
        if (i == right)
            break;
        i = (i + 1) % SIZE;
    }
    printf("\n");
}
