#include<stdio.h>

inline int maxi(int a, int b) {return a > b ? a : b;}

#define maxm(a,b)  (a > b ? a : b)

int main()

{

printf("\n The inline function result :is %f\n",maxi(5.5,6));

printf("\nTHe macro function result :is %f \n",maxm(5.5,6));

getchar();

return 0;

}