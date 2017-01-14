#ifndef LINKED_LIST
#define LINKED_LIST

typedef enum {false, true} bool;

typedef struct node {
    int val;
    struct node* next;
} Node;

typedef struct linkedlist {
    struct node* head;
} LinkedList;

int list_length(Node* head);
void print_list(Node* head);
void insert_node(Node** head, int position, int data);
void delete_node(Node** head, int position);
Node* find_middle(Node* head);

#endif