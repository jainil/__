#include <stdio.h>
#include <stdlib.h>
#include "linkedlist.h"

int main(void) {
    Node* first = (Node*)malloc(sizeof(Node));
    first->val = 1;
    Node* second = (Node*)malloc(sizeof(Node));
    second->val = 2;
    first->next = second;
    second->next = NULL;

    insert_node(&first, 2, 3);
    insert_node(&first, 3, 4);
    insert_node(&first, 4, 5);
    // insert_node(&first, 5, 6);
    // insert_node(&first, 6, 7);
    // insert_node(&first, 1, 4);
    // insert_node(&first, 0, 0);
    // insert_node(&first, 0, -1);
    // delete_node(&first, 0);
    
    // printf("%d\n", list_length(NULL));
    printf("%d\n", list_length(first));
    print_list(first);

    Node* middle = find_middle(first);
    printf("%d\n", middle->val);
    return 0;
}