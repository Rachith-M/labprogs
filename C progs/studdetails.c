#include <stdio.h>

struct Student {
    char name[100];
    int rollno;
    int marks;
};

void acceptDetails(struct Student *studentPtr) {
    printf("Enter student details\n");
    printf("Enter name: ");
    scanf("%s",(*studentPtr).name);
    printf("Enter Roll Number: ");
    scanf("%d",(*studentPtr).rollno);
    printf("Enter Marks: ");
    scanf("%d",(*studentPtr).marks);
}

void dispDetailsValue(struct Student student) {
    printf("Displaying details using call by value:\n");
    printf("Name: %s\n", student.name);
    printf("Roll Number: %d\n", student.rollno);
    printf("Marks: %d\n", student.marks);
}

void dispDetailsReference(const struct Student *studentPtr) {
    printf("Displaying details using call by reference:\n");
    printf("Name: %s\n", (*studentPtr).name);
    printf("Roll Number: %d\n", (*studentPtr).rollno);
    printf("Marks: %d\n", (*studentPtr).marks);
}

int main() {
    struct Student s1;
    acceptDetails(&s1);
    dispDetailsValue(s1);
    dispDetailsReference(&s1);
    return 0;
}

