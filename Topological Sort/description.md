# Topological sort

### Complexity: $O(|V| + |E|)$

### Idea

Given  a directed acyclic graph(DAG) G = (V, E) we find an order such that for every two vertices $v_1, v_2$ if $v_2 \succ v_1$ then there is no arc from $v_2$ to $v_1$ .

![image](sorted.png)

### Notes

If for every two consecutive sorted vertices there is an arc connecting them then the graph has Hamiltonian path and therefore its topological order is unique. Also should such path not exist there are at least two topological orderings.
