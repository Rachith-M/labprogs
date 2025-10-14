#include <stdio.h>
struct student1{
    char name1[20];
    int sub1[10];
};
void main(){
    struct student1 sem1;
    int n;
    printf("Enter the name of the student: \n");
    scanf("%s",&sem1.name1);
    printf("Enter the number of the subjects in 1st semester: \n");
    scanf("%d",&n);
    printf("Enter the marks: \n");
    for(int i = 0;i<n;i++){
        scanf("%d",&sem1.sub1[i]);
        }
    printf("The marks are: \n");
    for(int i = 0;i<n;i++){
        printf("%d \n",sem1.sub1[i]);
    }
}