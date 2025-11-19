#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node *next;
};

int main(){
    int choice,val;
    while(1){
        printf("Enter your choice:\n");
        printf("1. Insert front, 2. Insert Rear, 3. Delete front, 4. Delete rear, 5. Display, 6. Exit\n");
        scanf("%d",&choice);
        switch(choice){
            case 1: printf("Enter the value to be inserted at front:\n");
                    scanf("%d",&val);

                    break;

            case 2: printf("Enter the value to be inserted at rear:\n");
                    ins_rear(val);

                    break;

            case 3: int del_front();
                    break;

            case 4: int del_rear();
                    break;

            case 5: void display();
                    break;

            case 6: exit(0);

            default:printf("Invalid choice! Please try again!\n");
                    break;
        }
    }
}

void ins_front(struct node *head, int new_data){
    struct node *new_node = (struct node *)malloc(sizeof(struct node));

    new_node->data = new_data;
    new_node->next = head;
    return new_node;
}

void ins_rear(struct node *head, int new_data){
    struct node *new_node = (struct node *)malloc(sizeof(struct node));

    new_node->data = new_data;
    new_node->next = NULL;

    if(head == NULL){
        return new_node;
    }

    struct node *temp = head;  
    while(temp->next!=NULL){
        temp = temp->next;
    }
    return head;
}
