#include<stdio.h>

// main()
// {
// 	int num[40], i;

// 	for (i=0; i<=100; i++)
// 	   num[i] = i;
// }

main()
{
	int i=4, *j, *k;
	j = &i;
	k = j + 1;
	printf("%u\n",j);
	printf("%u",k);
	getchar();
}