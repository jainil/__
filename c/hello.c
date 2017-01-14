#include<stdio.h>
display(int* i){
	printf("%d\n", *i);
}
main(){
	char str[] = "Hello";
	char *p = "Hello";
	printf("%u\n",p);
	p = "bye";
	printf("%u\n",p);
	printf("%s\n", p);
	int array[] = {1,2,3};
	unsigned int* address = &array[1];
	display(address);


	getchar();
}