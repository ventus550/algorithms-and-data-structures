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

	def maxlist(L):
		mx = []
		for l in L:
			if len(l) > len(mx):
				mx = l
		return mx

	def DFS(v):
		return [v] + maxlist( DFS(u) for u in graph[v] )
	
	return maxlist( DFS(v) for v in range(len(graph)) ) # could be further optimised


print( longest(data) )
