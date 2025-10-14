#include <stdio.h>
struct student{
    char name[20];
    char USN[20];
    int aadhaar;
}stud[20];

int details(int n);
int display(int n);
void main(){
    int n;
    printf("Enter the number of students:\n");
    scanf("%d",&n);
    details(n);
    printf("The given student details are:\n");
    display(n);
}

int details(int n){
    int i;
    printf("Enter the student details:\n");
    for(i=0;i<n;i++){
        printf("Enter name:\n");
        scanf("%s",stud[i].name);
        printf("Enter USN:\n");
        scanf("%s",stud[i].USN);
        printf("Enter aadhaar:\n");
        scanf("%d",&stud[i].aadhaar);
    }
}

int display(int n){
    int i;
    for(i=0;i<n;i++){
        printf("Name: %s\n",stud[i].name);
        printf("USN: %s\n",stud[i].USN);
        printf("Aadhaar: %d\n",stud[i].aadhaar);
    }
}