#include <stdio.h>
#include <stdlib.h>
#define SIZE 10
int cirqueue[SIZE], front = -1, rear = -1;
void enqueue(int);
void dequeue();
void display();

int main(){
    int value,choice;
    while(1){
        printf("Enter your choice:\n");
        printf("1. Enqueue, 2. Dequeue, 3. Display, 4. Exit\n");
        scanf("%d",&choice);
        switch(choice){
            case 1: printf("Enter the value:\n");
                    scanf("%d",&value);
                    enqueue(value);
                    break;
            
            case 2: dequeue();
                    break;

            case 3: display();
                    break;

            case 4: exit(0);
            
            default:printf("Enter a valid choice!\n");
                    break;
        }
    }
}

void enqueue(int value){
    if(front == rear + 1 || front == 0 && rear == SIZE - 1){
        printf("Queue is full!\n");
    }
    else{
        if(front==-1){
            front = 0;
        }
        rear = (rear+1)%SIZE;
        cirqueue[rear] = value;
        printf("%d is inserted!\n",value);
    }
}

void dequeue(){
    if(front == -1){
        printf("Queue is empty!");
    }
    else{
        int element;
        element = cirqueue[front];
        if(front == rear){
            front = -1;
            rear = -1;
        }
        else{
            front = (front+1)%SIZE;
        }
        printf("%d has been deleted!\n",element);
    }
}

void display(){
    printf("The elements are:\n");
    printf("front is %d\n",front);
    for(int i = front; i!=rear; i = (i+1)%SIZE)
        printf("%d\t",cirqueue[i]);
    printf("\n");
    printf("rear is %d\n",rear);
}
