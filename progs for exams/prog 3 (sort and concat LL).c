#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int data;
    struct Node *next;
}Node;

void sort(Node *head){
    if(head == NULL){
        printf("LL is empty!\n");
        return;
    }
    Node *i,*j;
    int temp;
    for(i = head;i->next!=NULL;i = i->next){
        for(j = i->next; j!=NULL;j = j->next){
            if(i->data > j->data){
                temp = i->data;
                i->data = j->data;
                j->data = temp;
            }
        }
    }
}

void reverse(Node **head){
    if(*head == NULL){
        printf("LL is empty!\n");
        return;
    }
    Node *prev = NULL;
    Node *temp = *head;
    Node *next = NULL;
    while(temp!=NULL){
        next = temp->next;
        temp->next = prev;
        prev = temp;
        temp = next;
    }
    *head = prev;
}

Node *concat(Node **head1, Node **head2){
    if(*head1 == NULL){
        return *head2; 
    }
    if(*head2 == NULL){
        return *head1;
    }
    Node *temp = *head1;
    while(temp->next != NULL){
        temp = temp->next;
    }
    temp->next = *head2;
    return *head1;
}
