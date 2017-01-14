#include <stdio.h>
#include <stdlib.h>
#include "graph.h"
#include "linkedlist.h"

// http://www.geeksforgeeks.org/graph-and-its-representations/

// A utility function to print the adjacenncy list representation of graph
void printGraph(Graph* graph)
{
    int v;
    for (v = 0; v < graph->V; ++v)
    {
        Node* pCrawl = graph->Adj[v].head;
        printf("\n Adjacency list of vertex %d\n head ", v);
        while (pCrawl)
        {
            printf("-> %d ", pCrawl->val);
            pCrawl = pCrawl->next;
        }
        printf("\n");
    }
}
 
// Driver program to test above functions
int main()
{
    // create the graph given in above fugure
    int V = 5;
    Graph* graph = createGraph(V);
    addEdge(graph, 0, 1);
    addEdge(graph, 0, 4);
    addEdge(graph, 1, 2);
    addEdge(graph, 1, 3);
    addEdge(graph, 1, 4);
    addEdge(graph, 2, 3);
    addEdge(graph, 3, 4);
 
    // print the adjacency list representation of the above graph
    printGraph(graph);
 
    return 0;
}