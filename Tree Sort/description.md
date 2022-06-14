# Tree Sort

### Complexity: $O(n \cdot log(k))$
$n$ is the size of data and $k$ is the number of distinct keys

### Idea
Construct a BST where each node can contain multiple keys of the same value
thus the height of the tree is $O(log(k))$ on average.