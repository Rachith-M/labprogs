#include <stdio.h>
#include <stdlib.h>

#define SIZE 20

int queue[SIZE];
int front = -1, rear = -1;

void enqueue(int);
void dequeue();
void display();

int main(){
    int choice, a;

    while(1){
        printf("\nEnter your choice!\n");
        printf("1. Enqueue\n2. Dequeue\n3. Display\n4. Exit\n");
        scanf("%d", &choice);

        switch(choice){
            case 1:
                printf("Enter element to be queued:\n");
                scanf("%d", &a);
                enqueue(a);
                break;

            case 2:
                dequeue();
                break;

            case 3:
                display();
                break;

            case 4:
                exit(0);

            default:
                printf("Invalid choice! Please try again!\n");
        }
    }

    return 0;
}

void enqueue(int a){
    if(rear == SIZE - 1){
        printf("Queue is full!\n");
        return;
    }
    if(front == -1){ 
        front = rear = 0;
    }
    else{
        rear++;
    }
    queue[rear] = a;
    printf("%d enqueued\n", a);
}

void dequeue(){
    if(front == -1){
        printf("Queue is empty!\n");
        return;
    }
    printf("%d dequeued\n", queue[front]);
    if(front == rear){ 
        front = rear = -1;
    }
    else{
        front++;
    }
}

void display(){
    if(front == -1){
        printf("Queue is empty!\n");
        return;
    }
    printf("Queue elements:\n");
    for(int i = front; i <= rear; i++){
        printf("%d\t", queue[i]);
    }
    printf("\n");
}
