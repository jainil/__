#ifndef MY_FNP
#define MY_FNP 
typedef void (*my_fnp)(char*);

enum traffic_light_state {GREEN, YELLOW, RED};
enum me {SAD, HAPPY};

typedef struct node {
    int val;
    struct node* next;
} Node;
#endif