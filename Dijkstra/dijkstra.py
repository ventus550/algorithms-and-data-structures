from heapq import *
from math import inf

# adjacency matrix representation of a graph
# we mark missing edges with zeros
data = [
    #0  1  2  3  4  5
	[0, 7, 1, 0, 0, 0], #0
	[7, 0, 0, 2, 8, 0], #1
	[1, 0, 0, 6, 0, 0], #2
	[0, 2, 6, 0, 5, 3], #3
	[0, 8, 0, 5, 0, 4], #4
	[0, 0, 0, 3, 4, 0], #5
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


print(dijkstra(data, 0))