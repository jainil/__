// Write a program in C to call a functionA() when value of variable i is 1, call functionB() when value of i is 2 and call functionC() when value of i is 3. **without using if-else, for, while (or any loop or conditional statement), switch case, go to, Conditional operator.

#include<stdio.h>

int A() {
	printf("A\n");
	return 0;
}
int B() {
	printf("B\n");
	return 0;
}
int C() {
	printf("C\n");
	return 0;
}
int main() {
	int i=2;
	!(i-1)&&A();
	B()&&!(i-2);
	!(i-3)&&C();
	return 0;
	getchar();
}