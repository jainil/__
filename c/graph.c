#include <stdio.h>
#include <stdlib.h>
#include "graph.h"
#include "linkedlist.h"

Node* newAdjListNode(int dest) {
    Node* newNode = (Node*) malloc(sizeof(Node));
    newNode->val = dest;
    newNode->next = NULL;
    return newNode;
}

Graph* createGraph(int V) {
    Graph* graph =  (Graph*) malloc(sizeof(Graph));
    graph->V = V;
    graph->Adj = (LinkedList*) malloc(V*sizeof(LinkedList));

    int i;
    for (i = 0; i < V; ++i)
        graph->Adj[i].head = NULL;

    return graph;
}

void addEdge(Graph* G, int src, int dest) {
    Node* newNode = newAdjListNode(dest);
    newNode->next = G->Adj[src].head;
    G->Adj[src].head = newNode;
    
    newNode = newAdjListNode(src);
    newNode->next = G->Adj[dest].head;
    G->Adj[dest].head = newNode;
}
