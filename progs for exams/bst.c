#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    struct Node *left;
    struct Node *right;
    int data;
}Node;

Node *create(int value){
    Node *new_node = (Node *)malloc(sizeof(Node));
    new_node->data = value;
    new_node->left = NULL;
    new_node->right = NULL;
    return new_node;
}

Node *insert(Node *root,int value){
    if(root == NULL){
        root = create(value);
        return root;
    }
    if(value<root->data){
        root->left = insert(root->left,value);
    }
    if(value>root->data){
        root->right = insert(root->right,value);
    }
    return root;
}

void preorder(Node *root){
    if(root == NULL){
        return;
    }
    printf("%d \t",root->data);
    preorder(root->left);
    preorder(root->right);
}

void inorder(Node *root){
    if(root == NULL){
        return;
    }
    inorder(root->left);
    printf("%d \t",root->data);
    inorder(root->right);
}

void postorder(Node *root){
    if(root == NULL){
        return;
    }
    postorder(root->right);
    post(root->left);
    printf("%d \t",root->data);
}

int search(Node *root,int key){
    if(root == NULL){
        return 0;
    }
    if(root->data == key){
        return 1;
    }
    if(key<root->data){
        return search(root->left,key);
    }
    else{
        return search(root->right,key);
    }
}

Node *inordersuccessor(Node *root){
    while(root->left!=NULL){
        root = root->left;
    }
    return root;
}

Node *delete(Node *root,int value){
    if(value<root->data){
        root->left = delete(root->left,value);
    }
    else if(value>root->data){
        root->right = delete(root->right,value);
    }
    else{
        if(root->left == NULL && root->right == NULL){
            return NULL;
        }
        if(root->left == NULL){
            return root->right;
        }
        else if(root->right == NULL){
            return root->left;
        }
        Node *IS = inordersuccessor(root->right);
        root->data = IS->data;
        root->right = delete(root->right,IS->data);
    }
    return root;
}