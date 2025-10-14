#include <stdio.h>

// Define the student structure
struct student {
    char name[50];
    char usn[15];
    int marks;
};

void getStudentDetailsPtr(struct student *s_ptr) {
    printf("Enter name: ");
    scanf("%s", s_ptr->name);
    printf("Enter USN: ");
    scanf("%s", s_ptr->usn);
    printf("Enter marks: ");
    scanf("%d", &s_ptr->marks);
}


void displayStudentDetailsPtr(const struct student *s_ptr) {
    printf("\n--- Displaying Student Details ---\n");
    printf("Name: %s\n", s_ptr->name);
    printf("USN: %s\n", s_ptr->usn);
    printf("Marks: %d\n", s_ptr->marks);
}

int main() {
    struct student stud1;
    getStudentDetailsPtr(&stud1);
    displayStudentDetailsPtr(&stud1);
    return 0;
}