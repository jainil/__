#include <stdio.h>
#include <stdlib.h>
#include "linkedlist.h"

int list_length(Node* current) {
    // Node* current = *head;
    if (!current) {
        return 0;
    }
    int length = 0;
    while (current) {
        current = current->next;
        length++;
    }
    return length;
}

void print_list(Node* current) {
    // Node* current = *head;
    int i = 1;
    while (current) {
        printf("Node %d: %d\n", i, current->val);
        current = current->next;
        i++;
    }
}

void insert_node(Node** head, int position, int val) {
    if (!head) return;
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->val = val;
    Node* current = *head;

    if (position == 0) {
        newNode->next = current;
        *head = newNode; // head now points to newnode
        // head = &newNode; this just modifies the local head, does not updated the actual value of head in calling function because of call by value
    } else {
        int i = 0;
        while (current->next && i < position-1) {
            current = current->next;
            i++;
        }
        newNode->next = current->next;
        current->next = newNode;
    }
}

void delete_node(Node** head, int position) {
    Node* prev = NULL;
    Node* current = *head;

    int i = 0;
    while (current->next && i < position) {
        prev = current;
        current = current->next;
        i++;
    }
    if (prev) {
        prev->next = current->next;
    } else {
        *head = current->next;
    }
    free(current);
}

Node* find_middle(Node* head) {
    Node* slow = head;
    Node* fast = head;

    // Alternative way of initializing, though not sure if i like this..
    // Node *slow, *fast;
    // slow = fast = head;

    // we need the floor of the middle pointer, is there some way to do this better? ie w/o the if-else
    int isOdd = false;
    while(fast && fast->next) {
        if (isOdd == false) {
            fast = fast->next;
            isOdd = true;
        } else {
            fast = fast->next;
            slow = slow->next;
            isOdd = false;
        }
    }

    return slow;
}