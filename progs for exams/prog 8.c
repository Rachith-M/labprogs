#include <stdio.h>
#include <stdlib.h>
#define SIZE 10
int queue[SIZE],front = -1, rear = -1;

int enqueue(int);
int dequeue();
int display();

int main(){
	int value,choice;
	while(1){
		printf("Enter your choice:\n");
		printf("1.Enqueue,\n2.Dequeue,\n3.Display,\n4.Exit\n");
		scanf("%d",&choice);
		switch(choice){
			case 1: printf("Enter the value to be queued:\n");
					scanf("%d",&value);
					enqueue(value);
					break;

			case 2: dequeue();
					break;

			case 3: display();
					break;

			case 4: exit(0);

			default:printf("Invalid Choice! Please try again!\n");
					break;
		}
	}
}

int isEmpty(){
	if(front == -1){
		return 1;
	}
	return 0;
}

int isFull(){
    return ((rear + 1) % SIZE == front);
}

int enqueue(int value){
	if(isFull()){
		printf("Queue is Full!\n");
		return 0;
	}
	if(isEmpty()){
		front = 0;
		rear = 0;
	}
	else{
		rear = (rear+1)%SIZE;
	}
	queue[rear] = value;
}

int dequeue(){
	if(isEmpty()){
		printf("Queue is empty\n");
		return 0;
	}
	printf("%d successfully deleted from queue\n",queue[front]);
	if(front == rear){
		front = rear = -1;
	}
	else{
		front = (front+1)%SIZE;
	}
}

int display(){
	int i = front;
	if(isEmpty()){
		printf("Empty Queue!\n");
		return 0;
	}
	while(1){
		printf("%d\t",queue[i]);
		if(i==rear){
			break;
		}
		i = (i+1)%SIZE;
	}
	printf("\n");
}
