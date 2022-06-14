from queue import PriorityQueue


data = [10, 5, 10, 15, 5, 1, 16]

class Vertex:

	def __init__(self, weight, left = None, right = None):
		self.weight = weight
		self.left = left
		self.right = right
	
	def __lt__(self, other):
		return self.weight < other.weight
	
	
def build_tree(weights):

	# Initialize a priority queue Q with vertices
	Q = PriorityQueue(maxsize=len(weights))
	for w in weights:
		Q.put( Vertex(w) )
	
	# Contruct the tree
	while Q.qsize() > 1:
		v = Q.get()
		u = Q.get()
		p = Vertex(v.weight + u.weight, v, u)
		Q.put(p)

	# Retrieve the resulting Tree
	return Q.get()