#include "linkedlist.h"

#ifndef GRAPH
#define GRAPH

typedef struct graph {
    int V;
    int E;
    LinkedList* Adj;
} Graph;

Graph* createGraph(int V);
void addEdge(Graph* G, int src, int dest);

#endif