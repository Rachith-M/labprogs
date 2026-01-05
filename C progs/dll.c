#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int data;
    struct Node *next;
    struct Node *prev;
}Node;

void addFirst(Node **head,int value){
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode -> data = value;
    newNode -> next = NULL;
    newNode -> prev = NULL;
    if(*head == NULL){
        *head = newNode;
        return;
    }
    newNode -> next = *head;
    (*head) -> prev = newNode;
    *head = newNode;
}

void addLast(Node **head, int value){
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode -> data = value;
    newNode -> next = NULL;
    newNode -> prev = NULL;
    if(*head == NULL){
        *head = newNode;
        return;
    }
    Node *temp = *head;
    while(temp -> next != NULL){
        temp = temp -> next;
    }
    temp -> next = newNode;
    newNode -> prev = temp;
}

void deleteFirst(Node **head){
    if(*head == NULL){
        printf("Linked list is empty!\n");
        return;
    }
    Node *temp = *head;
    if((*head) -> next == NULL){
        *head = NULL;
    }
    else{
        (*head) -> next -> prev = NULL;
        *head = (*head) -> next;
    }
    printf("Deleted %d from LL!\n",temp -> data);
    free(temp);
}

void deleteLast(Node **head){
    if(*head == NULL){
        printf("LL is empty!\n");
        return;
    }
    Node *temp = *head;
    if((*head) -> next == NULL){
        *head = NULL;
    }
    else{
        while(temp -> next != NULL){
            temp = temp->next;
        }
        temp -> prev -> next = NULL;
    }
    printf("Deleted %d from LL!\n",temp -> data);
    free(temp);
}

void insPos(Node **head, int value, int pos){
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode -> data = value;
    newNode -> next = NULL;
    newNode -> prev = NULL;
    if(*head ==  NULL){
        addFirst(head,value);
        return;
    }
    Node *temp = *head;
    for(int i = 1;i < pos -1 && temp -> next!=NULL; i++ ){
        temp = temp->next;
    }
    if(temp ->next == NULL){
        addLast(head,value);
        return;
    }
    else{
        newNode -> next = temp -> next;
        newNode -> prev = temp;
        temp -> next -> prev = newNode;
        temp -> next = newNode;
    }
}

void insleft(Node **head, int value, int nodeval){
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = value;
    newNode->next = NULL;
    newNode->prev = NULL;
    if(*head == NULL){
        printf("List is empty!\n");
        return;
    }
    
    Node *temp = *head;

    if (temp->data = nodeval){
        newNode->next = *head;
        (*head)->prev = newNode;
        *head = newNode;
        return;
    }

    while(temp!=NULL && temp->data!=nodeval){
        temp = temp->next;
    }
    if(temp == NULL){
        printf("No such list!\n");
        return;
    }
    newNode->prev = temp->prev;
    newNode->next = temp;
    temp->prev->next = newNode;
    temp->prev = newNode;
}

void deletepos(Node **head, int nodeval){
    if(*head == NULL){
        printf("List is empty!\n");
        return;
    }
    
    Node *temp = *head;
    if(temp->data == nodeval){
        *head = temp->next;
        if(*head != NULL){
            (*head)->prev = NULL;
        }
        printf("%d deleted from list!",temp->data);
        free(temp);
        return;
    }

    while(temp!=NULL && temp->data!=nodeval){
        temp = temp->next;
    }
    if(temp == NULL){
        printf("No such values in the list!\n");
        return;
    }
    temp->prev->next = temp->next;

    if(temp->next != NULL){
        temp->next->prev = temp->prev;
    }

    printf("%d deleted from list!",temp->data);
    free(temp);
}

void display(Node *head){
    if(head == NULL){
        printf("List is empty!");
        return;
    }
    
    while(head!=NULL){
        printf("%d <-> ",head->data);
        head = head->next;
    }
    printf("NULL\n");
}