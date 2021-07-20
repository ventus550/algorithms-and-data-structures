# Intermidiate Vertices

### Complexity: $O(|V|)$

### Problem

Given a tree graph and a list of pairs $(v_1, u_1), ... , (v_n, u_n)$ decide whether $v_i$ is on the path from $u_i$ to root.


### Idea

While running DFS assign each to vertex its enter and exit times.