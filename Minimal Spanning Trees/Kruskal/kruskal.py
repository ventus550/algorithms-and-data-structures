# edges sorted by weight
data = [
	(0,2), (1,3),
	(3,5), (4,5),
	(4,3), (2,3),
	(0,1), (1,4)
]

def kruskal(graph):
	trees = {}; edges = []

	def tree(v):
		try:
			return trees[v]
		except:
			trees[v] = {v}
			return trees[v]

	for (v, u) in data:
		# check for cycle
		if tree(v) != tree(u):
			edges.append( (v, u) )

			# merge trees
			t = tree(v).union(tree(u))
			for v in t:
				trees[v] = t

	return edges

	
print(kruskal(data))