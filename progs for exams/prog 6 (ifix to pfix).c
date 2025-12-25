#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define SIZE 100

char stack[SIZE];
int top = -1;

void push(char c){
    stack[++top] = c;
}

char pop(){
    return stack[top--];
}

char peek(){
    return stack[top];
}

int isEmpty(){
    return top == -1;
}

int precedence(char op){
    if(op == '+' || op == '-'){
        return 1;
    }
    if(op == '*' || op == '/'){
        return 2;
    }
    return 0;
}

int main(){
    char infix[SIZE],postfix[SIZE];
    int i = -1, k = -1;
    char ch;

    printf("Enter a valid Infix Expression:\n");
    scanf("%s",infix);

    while((ch = infix[++i]) != '\0'){

        if(isalnum(ch)){
            postfix[++k] = ch;
        }
        else if(ch == '('){
            push(ch);
        }
        else if(ch == ')'){
            while(!isEmpty() && peek()!='('){ 
            postfix[++k] = pop();
            }
        pop();
        }
        else{
            while(!isEmpty() && precedence(peek())>=precedence(ch)){
                postfix[++k] = pop();
            }
            push(ch);
        }
    }
    while(!isEmpty()){
        postfix[++k] = pop();
    }
    postfix[++k] = '\0';

    printf("The postfix expression is: %s\n",postfix);
    
    return 0;
}