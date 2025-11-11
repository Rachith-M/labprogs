#include <stdio.h>
#include <string.h>
int pvalidation(char str[]){
    int i, top = -1;
    char s[20];
    for(i=0;i<strlen(str);i++){
        if(str[i] =='(' || str[i] =='[' || str[i] == '{'){
            s[++top] = str[i];
        }
        else if(str[i] == ')' && s[top] == '('){
            top--;
        }
        else if(str[i] == ']' && s[top] == '['){
            top--;
        }
        else if(str[i] == '}' && s[top] == '{'){
            top--;
        }
        else{
            return 0;
        }
    }
    if (top==-1){
        return 1;
    }
    else{
        return 0;
    }
}

int main(){
    char str[100];
    int res;
    printf("Enter an expression:\n");
    scanf("%s",str);
    res = pvalidation(str);
    if(res){
        printf("Paranthesis are balanced!\n");
    }
    else{
        printf("Paranthesis are not balanced!\n");\
    }
    return 0;
}