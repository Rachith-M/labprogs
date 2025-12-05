#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

struct Node *head = NULL;   // GLOBAL HEAD POINTER

void ins_front();
void ins_rear();
void del_front();
void del_rear();
void ins_atpos();
void display();

int main() {
    int choice;

    while(1) {
        printf("\nEnter your choice:\n");
        printf("1. Insert at front\n");
        printf("2. Insert at rear\n");
        printf("3. Delete from front\n");
        printf("4. Delete from rear\n");
        printf("5. Insert at position\n");
        printf("6. Display\n");
        printf("7. Exit\n");

        scanf("%d", &choice);

        switch(choice) {
            case 1: ins_front(); break;
            case 2: ins_rear(); break;
            case 3: del_front(); break;
            case 4: del_rear(); break;
            case 5: ins_atpos(); break;
            case 6: display(); break;
            case 7: exit(0);

            default: printf("Invalid choice! Try again.\n");
        }
    }
    return 0;
}

void ins_front(){
    int value;
    printf("Enter the value to be inserted:\n");
    scanf("%d",&value);

    struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
    new_node->data = value;
    new_node->next = head;
    head = new_node;

    printf("%d inserted at front of the linked list!\n",value);
}

void ins_rear(){
    int value;
    printf("Enter the value to be inserted:\n");
    scanf("%d",&value);

    struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
    new_node->data = value;
    new_node->next = NULL;

    if(head == NULL){
        head = new_node;
        return;
    }
    
    struct Node *temp = head;
    while(temp->next!=NULL){
        temp = temp->next;
    }
    temp->next = new_node;
    printf("%d successfully inserted at the end of the linked list!\n",value);
}

void del_front(){
    if(head == NULL){
        printf("List is Empty!\n");
        return;
    }
    struct Node *temp = head;
    head = head->next;
    printf("%d deleted from the front of the linked list!\n",temp->data);
    free(temp);
}

void del_rear(){
    if(head == NULL){
        printf("List is empty!\n");
        return;
    }
    if(head->next==NULL){
        free(head);
        head = NULL;
        return;
    }
    struct Node *temp = head;
    struct Node *prev = NULL;
    while(temp->next!=NULL){
        prev = temp;
        temp = temp->next;
    }
    printf("%d deleted from the linked list!\n",temp->data);
    prev->next = NULL;
    free(temp);
}

void ins_atpos(){
    int pos,value;
    printf("Enter the position to be inserted at:\n");
    scanf("%d",&pos);
    printf("Enter the value to be inserted:\n");
    scanf("%d",&value);
    
    struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
    new_node->data = value;

    if(pos == 1){
        new_node->next = head;
        head = new_node;
        printf("%d inserted at front!\n",value);
        return;
    }

    struct Node *temp = head;
    for(int i = 1;i<pos-1;i++){
        if(temp == NULL){
            printf("Invalid position!\n");
            free(new_node);
            return;
        }
        temp = temp->next;
    }
    new_node->next = temp->next;
    temp->next = new_node;
    
    printf("%d inserted at position %d!\n",value,pos);
}

void display(){
    if(head == NULL){
        printf("Linked list is Empty!\n");
        return;
    }
    struct Node *temp = head;
    int count = 0;
    while(temp!=NULL){
        printf("%d|%p -> ",temp->data,temp->next);
        count++;
        temp = temp->next;
    }
    printf("NULL\n");
    printf("The number of nodes are %d",count);
    printf("%d");
}