from heapq import *
from math import inf

# adjacency matrix representation of a graph
# we mark missing edges with zeros
data = [
    #0  1  2  3  4
	[0, 1, 8, 3, 7], #0
	[1, 0, 1, 2, 0], #1
	[8, 1, 0, 1, 2], #2
	[3, 2, 1, 0, 1], #3
	[7, 0, 2, 1, 0], #4
]

def dijkstra(graph, source):
	size = len(graph)
	dist = [inf] * size
	parent = [None] * size
	dist[source] = 0

	Q = [(0, source)]; heapify(Q)
	while Q:
		v = heappop(Q)[1]
		for u in range(size):
			weight = data[v][u]
			alt = dist[v] + weight

			if weight and alt < dist[u]:	
				parent[u] = v
				dist[u] = alt
				heappush(Q, (alt, u))


	return dist