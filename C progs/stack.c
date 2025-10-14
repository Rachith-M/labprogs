#include <stdio.h>
#include <stdlib.h>
#define SIZE 10
void push(int);
void pop();
void display();
int stack[SIZE],top = -1;

void main(){
    int choice,value;
    while(1){
        printf("Enter your choice:\n");
        printf("Your choices are: \n1.Push, 2.Pop, 3.display, 4.exit\n");
        scanf("%d",&choice);
        switch(choice){
            case 1: printf("Enter the value to be inserted:\n");
                    scanf("%d",&value);
                    push(value);
                    break;

            case 2: pop();
                    break;

            case 3: display();
                    break;
        
            case 4: exit(0);
                    break;
        
            default: printf("Invalid input! Please try again!\n");
                    break;                       
        }
    }
}  

void push(int value){
    if(top==SIZE-1){
        printf("Stack overflow!\n");
    }
    else{
        top++;
        stack[top] = value;
    }
}

void pop(){
    if(top==0){
        printf("Stack underflow!\n");
    }
    else{
        top--;
    }
}

void display(){
    if(top==-1){
        printf("Empty Stack!\n");
    }
    else{
        for(int i = 0;i<=top;i++){
            printf("%d\n",stack[i]);
        }
    }
}