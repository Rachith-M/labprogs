#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
int stack[20], top = -1;

int push(int a){
    stack[++top] = a;
}

int pop(){
    return stack[top--];
}

void main(){
    int i,n1,n2,n3,num;
    char *e, exp[20];
    printf("Enter the expression:\n");
    scanf("%s",exp);
    e = exp;
    
    while(*e!='\0'){
        if(isdigit(*e)){
            num = *e - 48;
            push(num);
        }
        else{
            n1 = pop();
            n2 = pop();
            switch(*e){
                case '+': n3 = n1 + n2;
                            break;
                
                case '-': n3 = n2-n1;
                            break;

                case '*': n3 = n1*n2;
                            break;

                case '/': n3 = n2/n1;
                            break;
            }
            push(n3);
        }
        e++;
    }
    printf("The result of given expression is: %d\n",pop());
}
