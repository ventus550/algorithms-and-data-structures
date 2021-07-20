# Dijkstra

### Complexity: $O(|V|log|V| + |E|)$

### Idea

Dijkstra is a solution to the problem of finding the shortest paths from source.
The algorithm can be thought of as a single expanding super vertex. Lets name it S.
We start by setting source distance to 0 and adding it to S.
We proceed by selecting the shortest edge from S and adding its vertex to S and updating S's edges.
This process continues until there are no vertices outside of S.

### Correctness

***Proof by contradiction***

Let D[v] be the distance computed by the algorithm and Opt[v] the real distance.

Hypothesis: For each $v$ D[v] = Opt[v]

Assume contrary, let $v$ be the first vertex for which D[v] != Opt[v]
Obviously $v$ is not the source since D[source] = 0 = Opt[v].
We know that for all parents $p$ of $v$ we have D[p] = Opt[p] and that the algorithm chooses the lightest edge from the visited parent vertices.

If the optimal parent is amongst already computed nodes then its edge's weight is greater that the one chosen by the algorithm which is contradicting assumption of that path being optimal.

If the optimal parent belongs to vertices not yet computed then its distance from source has to be greater than $v$.
If thats the case then there can be no shorter path to $v$ leading through that parent, thus we have a contradiction with the assumption that D[v] != Opt[v].