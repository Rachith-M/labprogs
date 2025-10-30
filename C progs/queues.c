#include<stdio.h>
#define size 20
 void insert(int);
 void del();
 void disp();

 int queue[size],front=0,rear=-1;
 void main()
 {
     int value,cho;
     while(1)
     {
         printf("\n1.insert\n2.delete\n3.display\n4.exit\nEnter the choice:");
         scanf("%d",&cho);
         switch(cho)
         {
             case 1:printf("Enter a value to enter: ");
                    scanf("%d",&value);
                    insert(value);
                    break;
            case 2:del();
                   break;
            case 3:disp();
                   break;
            case 4:exit(0);
            default:
                printf("Invalid input..Enter a correct choice");
         }
     }
 }

 void insert(int value)
 {
     if (rear==size-1)
        printf("Queue is full.You can't insert");
     else
     {
         queue[++rear]=value;
     }
 }

 void del()
 {
     if (front==size-1 || front>rear)
        printf("Queue is empty.You can't delete");
     else
     {

         printf("\n%d removed\n",queue[front]);
         front++;


     }
 }
void disp()
{
    if (front>rear)
        printf("The queue is empty\ncan't display elements ");
    else
    {
        printf("The elements are:");
        for(int i=front;i<=rear;i++)
            printf("%d\t",queue[i]);

    }

}
