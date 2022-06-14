from tsort import tsort

# adjacency list representation of a graph
data = [
	[1, 2], # {0->1, 0->2}
	[2, 5], # {1->2, 1->5}
	[3],    # {2->3}
	[],     # {}
	[],     # {}
	[3, 4], # {5->3, 5->4}
	[1, 5]  # {6->1, 6->5}
]

def longest(graph):
	n = len(graph)
	tsorted = tsort(data)
	maxlen = [ [] for _ in range(n) ]

	for v in tsorted:
		maxlen[v].append(v)

		for u in graph[v]:
			maxlen[u] = max( maxlen[u], maxlen[v] ).copy()
	
	return max(maxlen)


print(longest(data) )
