#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include "example.h"
#include "example2.h"

void str_reverse(char* str_in);
void str_reverse_through_pointer(char* str_in);
static void swap_two_numbers(int*, int*);

static int b = 2;

int main (int argc, char** argv) {
    // printf("argc: %d\n", argc);
    // int i;
    // char* input;
    // for (i=0; i<argc; i++) {
    //     printf("argv: %s\n", argv[i]);
    //     if (i==1) input = argv[i];
    // }
    // str_reverse_through_pointer(input);
    // printf("reversed input: %s\a\n", input);

    // enum me cool = SAD;
    // Node n;
    // n.val = 4;
    // n.next = NULL;
    // Node* np = &n;
    // printf("%d\n", np->val);


    // int64_t a = 0xFA;
    // extern int b;
    // printf("a: %d, b: %d\n", a, b);
    // swap_two_numbers(&a, &b);
    // printf("a: %d, b: %d\n", a, b);

    int test = 1;
    int* testp = &test;
    int test2 = 2;

    printf("%d\n", *testp);
    printf("%p\n", testp);
    printf("%p\n", &testp);

    testp = &test2;
    printf("%d\n", *testp);
    printf("%d\n", test);
    printf("%p\n", &testp);
}

void str_reverse(char* str_in) {
    char tmp;
    int ii = 0;
    size_t len  = strlen(str_in);
    for (ii = 0; ii < len/2; ii++) {
        tmp = str_in[ii];
        str_in[ii] = str_in[len-1 - ii];
        str_in[len-1-ii] = tmp;
    }
}

void str_reverse_through_pointer(char* str_in) {
    // void (*f)(char*);
    my_fnp f = &str_reverse;
    (*f)(str_in);
}

void swap_two_numbers(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}