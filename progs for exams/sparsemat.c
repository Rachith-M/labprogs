#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int value;
    int row;
    int col;
    struct Node *next;
}Node;

void create(struct Node **head, int val, int row_ind, int col_ind){
    Node *r = (Node *)malloc(sizeof(Node));
    r->value = val;
    r->row = row_ind;
    r->col = col_ind;
    r->next = NULL;
    if(*head == NULL){
        *head = r;
    }

    else{
        Node *temp = *head;
        while(temp->next!=NULL){
            temp = temp->next;
        }
        temp->next = r;
    }
}

void display(struct Node *start)
{
    struct Node *temp = start;

    printf("\nRow  Column  Value\n");
    while (temp != NULL) {
        printf("%d      %d       %d\n",
               temp->row,
               temp->col,
               temp->value);
        temp = temp->next;
    }
}

void main(){
    Node *head = NULL;
    int sparse[4][5] = {
        {0, 0, 3, 0, 4},
        {0, 0, 5, 7, 0},
        {0, 0, 0, 0, 0},
        {0, 2, 6, 0, 0}
    };
    
    int rows = 4;
    int cols = 5;

    for(int i = 0;i<rows;i++){
        for(int j = 0;j<cols;j++){
            if(sparse[i][j]!=0){
                create(&head,sparse[i][j],i,j);
            }
        }
    }
    display(head);
}
