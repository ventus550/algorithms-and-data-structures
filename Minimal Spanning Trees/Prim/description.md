# Prim

### Complexity
Generally $O(|V|^2)$ but get be reduced using suitable data structures:
- binary heap and adjacency list -- $O(|E|log|V|)$
- Fibonacci heap and adjacency list -- $O(|E| + |V|log|V|)$

### Idea

We start by imagining graph as an expanding tree. At first said tree includes only one vertex (chosen arbitrarily). In each iteration we choose the lightest edge connecting tree to the outer vertices. The tree then expands including adjacent vertex. This process continues until there are no edges to choose from. 


### Notes
Variety of implementations and time complexities allows tailoring of algorithm to perform better when the number of vertices and edges is known.
