// #include<stdio.h>

// #define TOTAL_ELEMENTS (sizeof(array) / sizeof(array[0]))
// int array[] = {23,34,12,17,204,99,16};

// int main()
// {
//     unsigned int d;

//     printf("%d\n", TOTAL_ELEMENTS );

//     for(d=0;d <= (TOTAL_ELEMENTS-1);d++)
//         printf("%d\n",array[d]);

//     getchar();
//     return 0;
// }

#include<stdio.h>

// void OS_Solaris_print()
// {
//         printf("Solaris - Sun Microsystems\n");
// }

// void OS_Windows_print()
// {
//         printf("Windows - Microsoft\n");

// }
// void OS_HP_UX_print()
// {
//         printf("HP-UX - Hewlett Packard\n");
// }

// int main()
// {
//         int num;
//         printf("Enter the number (1-3):\n");
//         scanf("%d",&num);
//         switch(num)
//         {
//                 case 1:
//                         OS_Solaris_print();
//                         break;
//                 case 2:
//                         OS_Windows_print();
//                         break;
//                 case 3:
//                         OS_HP_UX_print();
//                         break;
//                 default:
//                         printf("Hmm! only 1-3 :-)\n");
//                         break;
//         }

//         return 0;
// }

enum {false,true};

int main()
{
        int i=1;
        do
        {
                printf("%d\n",i);
                i++;
                if(i < 15)
                        continue;
        }while(false);
        getchar();
        return 0;
}