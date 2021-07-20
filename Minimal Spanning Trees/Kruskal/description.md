# Kruskal

### Complexity: $O(|E|log|E|)$

### Idea

We start by imagining graph as a set of trees where each tree is just a single vertex. We iterate through edges always picking the lightest one and check if the edge can be used to connect a pair of trees. An edge is usable if and only if it does not create a cycle. This condition can be easily verified by making sure that the connected vertices belong to diffrent trees. Once the connection is found we merge the trees and the process continues until no edges are left unverfied.


### Notes

Many similarities with Boruvka's algorithm which might be a better option when introducing parallel programming.
