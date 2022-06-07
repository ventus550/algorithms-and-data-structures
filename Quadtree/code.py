from numpy import array, float64, reshape, array_equal as equal

class Quadtree:
	def __init__(self, shape : tuple):
		self.shape = array(shape, dtype=float64)
		self.center = self.shape / 2
		self.data = (None, None)
		self.size = 0

	def empty(self):
		return self.data[0] is None
	
	def leaf(self):
		return type(self.data) == tuple

	def quadrant(self, key):
		assert not self.leaf()
		x, y = key > self.center
		return int(x), int(y)
	
	def subtree(self, quadrant):
		return self.data[quadrant]

	def subkey(self, key, quadrant):
		return key - quadrant * self.center
	
	def find(self, key):
		node = self
		while not node.leaf():
			quad = node.quadrant(key)
			key = node.subkey(key, quad)
			node = node.subtree(quad)
		return node, key

	def split(self):
		assert self.leaf() and not self.empty()
		subtrees = [Quadtree(self.shape / 4) for _ in range(4)]
		(key, value), self.data = self.data, reshape(subtrees, (2, 2))
		self[key] = value

	def __setitem__(self, key, value):
		node, subkey = self.find(key)
		if node.empty() or equal(node.data[0], subkey):
			node.data = (subkey, value)
		else:
			node.split()
			node[subkey] = value

	def __getitem__(self, key):
		node, subkey = self.find(key)
		key, value = node.data
		return value if equal(key, subkey) else None




Q = Quadtree((100, 100))

Q[75, 75] = 'A'
Q[1, 10] = 'B'
Q[2, 10] = 'C'
print(Q[75, 75], Q[1, 10], Q[2,10])


Q[1, 10] = 'X'
print(Q[75, 75], Q[1, 10], Q[2,10])