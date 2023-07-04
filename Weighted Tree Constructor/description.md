# Weighted Tree Constructor

### Complexity: $O(nlogn)$

### Problem
Given a set of weigths W contruct a binary tree where each leaf is given exactly one of those weights while also minimalizing *external length* (EL) where $w(v)$ is the weight function and $d(v)$ is the distance from root to $v$.

$$ EL(T) = \sum_{v \in leaves(T)} w(v)d(v) $$

### Algorithm
1. Initialize a priority queue Q with vertices with weights in W
2. while $|Q| > 1$ repeat:
	- pop two lightest elements $v$, $u$
	- create a parent $p$ of $v$, $u$ and set its weight to $w(p)$
	- insert p into Q
3. Pop the only element left in Q. The popped element is the resulting tree
