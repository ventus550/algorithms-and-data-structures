from queue import Queue

def tsort(graph):

	tsorted = []

	# make an arcs list
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