# Floyd-Warshall

### Complexity: $O(|V|^3)$

### Idea

Let D[k][v][u] be the shortest distance from v to u through node k.
From here we use dynamic programming to solve the recursive definition:
	D[k][v][u] = min(D[k-1][v][u], D[k-1][v][k] + D[k-1][k][u])
