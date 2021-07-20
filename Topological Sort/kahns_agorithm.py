from queue import Queue

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

def kahn(graph):

	tsorted = []

	# make a arcs list
	arcs = [0]*len(graph)
	for v in graph:
		for adj in v:
			arcs[adj] += 1

	# initialize FIFO queue
	Q = Queue()
	for vi in range(len(graph)):
		if arcs[vi] == 0: # at least one vertex satisfying this condition
			Q.put(vi)
	
	# actual sorting
	while not Q.empty():
		vi = Q.get()
		tsorted.append(vi)
		v = graph[vi]

		for adj in v:
			arcs[adj] -= 1
			if arcs[adj] == 0:
				Q.put(adj)
	
	return tsorted
