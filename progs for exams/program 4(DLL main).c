#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int data;
    struct Node *next;
    struct Node *prev;
}Node;

void addFirst(Node **head, int val){
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = val;
    newNode->next = NULL;
    newNode->prev = NULL;
    if(*head == NULL){
        *head = newNode;
        return;
    }
    (*head)->prev = newNode;
    newNode->next = (*head);
    *head = newNode;
}

void addLeft(Node **head, int val, int query){
    if(*head == NULL){
        printf("LL is empty! No such values exist!\n");
        return;
    }
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = val;
    newNode->next = NULL;
    newNode->prev = NULL;
    if((*head)->data == query){
        newNode->next = *head;
        (*head)->prev = newNode;
        *head = newNode;
        return;
    }
    Node *temp = *head;
    while(temp!=NULL && temp->data!=query){
        temp = temp->next;
    }
    if(temp == NULL){
        printf("No such element exists in LL!\n");
        return;
    }
    else{
        newNode->next = temp;
        newNode->prev = temp->prev;
        temp->prev->next = newNode;
        temp->prev = newNode;
    }
}


void deleteVal(Node **head,int query){
    if(*head == NULL){
        printf("LL is empty! No such values exist!\n");
        return;
    }
    if((*head)->data == query){
        printf("%d deleted from LL!\n",(*head)->data);
        if((*head)->next == NULL){
            *head = NULL;
            return;
        }
        else{
            *head = (*head)->next;
            (*head)->prev = NULL;
            return;
        }
    }
    Node *temp = *head;

    while(temp!=NULL && temp->data != query){
        temp = temp->next;
    }
    if(temp == NULL){
        printf("No such elements in LL!\n");
        return;
    }
    if(temp->next == NULL){
        printf("%d deleted from LL!\n",temp->data);
        temp->prev->next = NULL;
        free(temp);
        return;
    }
    else{
        printf("%d deleted from LL!\n",temp->data);
        temp->prev->next = temp->next;
        temp->next->prev = temp->prev;
        free(temp);
        return;
    }
}

void display(Node *head){
    if(head == NULL){
        printf("LL is empty!\n");
        return;
    }
    Node *temp = head;
    while(temp!=NULL){
        printf("%d<->",temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}