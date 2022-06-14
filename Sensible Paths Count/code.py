# Path is sensible when each vertex is closer to the destination than the previous
from dijkstra import dijkstra

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

# Count the number of sensible paths from source to destination
def CountPaths(graph, source, destination):

	n = len(graph)
	dist = dijkstra(graph, destination)
	graph = [ [i for i in range(n) if v[i]] for v in graph ] # matrix to list representation :(
	sensibles = [None]*n; sensibles[destination] = 1

	def dfs(v):

		if sensibles[v] != None:
			return sensibles[v]
		
		s = 0
		for w in graph[v]:
			if dist[w] < dist[v]:
				s += dfs(w)

		sensibles[v] = s
		return s

	
	return dfs(source)


print(CountPaths(data, 4, 0))