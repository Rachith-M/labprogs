#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int coef;
    int exp;
    struct Node *next;
}Node;

void addFirst(Node **head, int c , int e){
    Node *new_node = (Node *)malloc(sizeof(Node));
    new_node->coef = c;
    new_node->exp = e;
    if(*head == NULL){
        *head = new_node;
        return;
    }
    new_node->next = *head;
    *head = new_node;
    return;
}

void display(Node *head){
    if(head == NULL){
        printf("Empty LL!\n");
        return;
    }
    Node *temp = head;
    while(temp!=NULL){
        printf("%d x %d \t",temp->coef,temp->exp);
        temp = temp->next;
    }
    return;
}

void addPoly(Node *poly1, Node *poly2){
    Node *poly3 = NULL;
    while(poly1!=NULL && poly2!=NULL){
        if(poly1->exp == poly2->exp){
            addFirst(&poly3,poly1->coef+poly2->coef,poly1->exp);
            poly1 = poly1->next;
            poly2 = poly2->next;
        }
        else if(poly1->exp>poly2->exp){
            addFirst(&poly3,poly1->coef,poly1->exp);
            poly1 = poly1->next;
        }
        else{
            addFirst(&poly3, poly2->coef, poly2->exp);
            poly2 = poly2->next;
        }
    }

    while(poly1!=NULL){
        addFirst(&poly3,poly1->coef,poly1->exp);
        poly1 = poly1->next;
    }

    while(poly2!=NULL){
    addFirst(&poly3,poly2->coef,poly2->exp);
    poly2 = poly2->next;
    }
}
