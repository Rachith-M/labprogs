#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int data;
    struct Node *next;
}Node;

void addFirst(Node **head,int val){
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = val;
    newNode->next = NULL;
    if(*head == NULL){
        *head = newNode;
        return;        
    }
    newNode->next = *head;
    *head = newNode;
}

void addLast(Node **head,int val){
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = val;
    newNode->next = NULL;
    if(*head == NULL){
        *head = newNode;
        return;
    }
    Node *temp = *head;
    while(temp->next != NULL){
        temp = temp->next;
    }
    temp->next= newNode;
}

void addPos(Node **head,int val,int pos){
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = val;
    newNode->next = NULL;
    if(*head == NULL){
        *head = newNode;
        return;
    }
    if(pos == 1){
        addFirst(head,val);
        return;
    }
    Node *temp = *head;
    Node *prev = NULL;
    for(int i = 1; i<pos - 1 && temp!=NULL;i++){
        prev = temp;
        temp = temp->next;
    }
    if(temp==NULL){
        printf("Invlid Position!\n");
        return;
    }
    if(temp->next == NULL){
        addLast(head,val);
        return;
    }
    newNode->next = prev->next;
    prev->next = newNode;    
}

void deleteFirst(Node **head){
    if(*head == NULL){
        printf("LL is empty!\n");
        return;
    }
    Node *temp = *head;
    *head = (*head)->next;
    printf("%d has been deleted!\n",temp->data);
    free(temp);
}

void deleteLast(Node **head){
    if(*head == NULL){
        printf("LL is empty!\n");
        return;
    }
    if((*head)->next == NULL){
        printf("%d deleted from LL!\n",(*head)->data);
        (*head) = (*head)->next;
        return;
    }
    Node *temp = *head;
    Node *prev = NULL;
    while(temp->next != NULL){
        prev = temp;
        temp = temp->next;
    }
    printf("%d deleted from LL!\n",temp->data);
    prev->next = NULL;
    free(temp);
}

void deleteEle(Node **head,int val){
    if(*head == NULL){
        printf("LL is empty!\n");
        return;
    }
    Node *temp = *head;
    Node *prev = NULL;
    if(temp->data == val){
        printf("%d deleted from LL!\n",temp->data);
        *head = temp->next;
        free(temp);
        return;
    }
    while(temp!= NULL && temp->data != val){
        prev = temp;
        temp = temp->next;
    }
    if(temp == NULL){
        printf("Element doesn't exist in LL!\n");
        return;
    }
    else if(temp->data == val){
        printf("%d deleted from LL!\n",temp->data);
        prev->next = temp->next;
        free(temp);
    }
}

void display(Node *head){
    if(head == NULL){
        printf("LL is empty!\n");
        return;
    }
    Node *temp = head;
    while(temp!=NULL){
        printf("%d->",temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

