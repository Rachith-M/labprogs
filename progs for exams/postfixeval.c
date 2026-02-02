#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int stack[20],top = -1;

int push(int a){
    stack[++top] = a;
}

int pop(){
    return stack[top--];
}

void main(){
    char s[20];
    int res, i = 0,x;
    float n1,n2,n3;
    printf("Enter a valid postfix expression:\n");
    scanf("%s",s);
    while(s[i]!='\0'){
        if(isdigit(s[i])){
            x = s[i] - '0';
            push(x);
        }
        else{
            n2 = pop();
            n1 = pop();
            switch(s[i]){
                case '+':   n3 = n1 + n2;
                            break;
                
                case '-':   n3 = n1 - n2;
                            break;

                case '*':   n3 = n1*n2;
                            break;

                case '/':   n3 = n1/n2;
                            break;

            }
            push(n3);
        }
        i++;   
    }
    printf("The result of given postfix expression is: %d\n",pop());
}