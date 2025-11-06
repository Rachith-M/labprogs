#include <stdio.h>

void towers(int num, char frompeg, char topeg, char auxpeg);

int main(){
    int num;
    printf("Enter the number of disks:\n");
    scanf("%d",&num);
    printf("The sequence of moves involved in the Tower of Hanoi are:\n");
    towers(num,'A','C','B');
}

void towers(int num, char frompeg, char topeg, char auxpeg){
    if(num == 1){
        printf("Move disk 1 from %c to %c\n",frompeg, topeg);
    }
    else{
        towers(num - 1, frompeg, auxpeg, topeg);
        printf("Move disk %d from %c to %c\n", num, frompeg, topeg);
        towers(num - 1, auxpeg, topeg, frompeg);
    }
}