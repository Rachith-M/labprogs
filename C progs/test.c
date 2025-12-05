#include <stdio.h>
#include <stdlib.h>
#define SIZE 5
int deque[SIZE], front = -1, rear = -1; //here left = front and rear = right

int ins_left(int);
int ins_right(int);
int del_left();
int del_right();
int display();
int isEmpty();
int isFull();

int main(){
    int choice, val_r, val_l;
    while(1){
        printf("Enter your choice:\n");
        printf("1.Queue from right,\n2.Queue from left,\n3.Dequeue from right,\n4.Dequeue from left,\n5.Display,\n6.Exit\n");
        scanf("%d",&choice);
        switch(choice){
            case 1: printf("Enter the element to be queued from right:\n");
                    scanf("%d",&val_r);
                    ins_right(val_r);
                    break;

            case 2: printf("Enter the element to be queued from left:\n");
                    scanf("%d",&val_l);
                    ins_left(val_l);
                    break;

            case 3: del_right();
                    break;
            
            case 4: del_left();
                    break;
            
            case 5: display();
                    break;

            case 6: exit(0);
                    break;

            default:printf("Invalid Choice! Please try again!\n");
                    break;
        }
    }
}

int isEmpty(){
    if((front == -1) && (rear == -1)){
        return 1;
    }
    return 0;
}

int isFull(){
    if((front == (rear+1)%SIZE) && (rear == SIZE - 1)){
        return 1;
    }
    return 0;
}

int ins_left(int value){
    if(isFull()){
        printf("Queue overflow!\n");
        return 0;
    }
    if(isEmpty()){
        front = rear = 0;
    }
    else{
        rear = (rear+1)%SIZE;
    }
    deque[rear] = value;
}

int ins_right(int value){
    if (isFull()){
		printf("Queue overflow!\n");
		return 0;
	}
    if(isEmpty()){
        front = rear = 0;
    }
	else{
        front = (front - 1 + SIZE)%SIZE;
    }
    deque[front] = value;
}

int del_left(){
    if(isEmpty()){
        printf("Queue underflow!\n");
        return 0;
    }
    printf("%d deleted from the queue!\n",deque[front]);
    if(front == rear){
        front = rear = -1;
    }
    else{
        front = (front+1)%SIZE;
    }
}

int del_right(){
    if(isEmpty()){
        printf("Queue undeflow!\n");
        return 0;
    }
    printf("%d deleted from the queue!\n",deque[rear]);
    if(front == rear){
        front = rear = -1;
    }
    else{
        rear = (rear - 1 + SIZE)%SIZE;
    }
}

int display(){
    if(isEmpty()){
        printf("Queue is Empty!\n");
        return 0;
    }
    printf("Your Queue is:\n");
    int i = front;
    while(1){
        printf("%d\t",deque[i]);
        if(i == rear){
            break;
        }
        i = (i+1)%SIZE;
    }
    printf("\n");
}