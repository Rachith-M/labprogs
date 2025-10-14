#include <stdio.h>
#include <math.h>
#include <string.h>
#include <ctype.h>

double compute(char symbol, double op1, double op2);
double compute(char symbol, double op1, double op2){
    switch(symbol){
        case '+': return op1+op2;
        break;
        case '-': return op1-op2;
        break;
        case '*': return op1*op2;
        break;
        case '/': return op1/op2;
        break;
        case '^': return pow(op1,op2);
        break;
    }
}