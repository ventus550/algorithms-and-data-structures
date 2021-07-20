from queue import Queue

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

def prim(graph):
	edges = []
	branches = set()

	def weight(v, u):
		return data[v][u]

	def expand(v):
		nonlocal branches
		# prepare new edges
		expanded = set([ (v, u) for u in range(len(data[v])) if weight(v, u) != 0])
		# remove all edges extending to v
		branches = set([ (e[1], e[0]) if e[1] == v else e for e in branches ]) ^ expanded

	expand(0)
	while branches:
		best = min(branches, key=lambda e: weight(e[0], e[1]))
		edges.append(best)
		expand(best[1])
	
	return edges

	
print(prim(data))