#include <stdio.h>
#include <stdlib.h>
#define SIZE 20
int queue[SIZE], front = -1, rear = -1;
void enqueue(int);
void dequeue();
void display();
void main(){
    int choice,a;
    while(1){
        printf("Enter your choice!\n");
        printf("1. Enqueue, 2. Dequeue, 3. Display, 4. Exit\n");
        scanf("%d",&choice);
        switch(choice){
            case 1: printf("Enter element to be queued:\n");
                    scanf("%d",&a);
                    enqueue(a);
                    break; 

            case 2: dequeue();
                    break;

            case 3: display();
                    break;

            case 4: exit(0);
            
            default: printf("Invalid choice! Please try again!\n");
        }
    }
}

void enqueue(int a){
    if(rear == SIZE - 1){
        printf("Queue is full!\n");
    }
    else if(front==-1){
        front++;
        rear++;
        queue[rear] = a;
    }
    else{
        rear++;
        queue[rear] = a;
    }
}

void dequeue(){
    if(front > rear || front == -1){
        printf("Queue is empty!\n");
    }

    else{
        front++;
    }
}

void display(){
    for(int i = front;i<=rear;i++){
        printf("%d\t",queue[i]);
    }
    printf("\n");
}