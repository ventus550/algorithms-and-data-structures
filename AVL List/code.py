
def zeroleaf(func):
	def inner(node):
		if node is AVL.leaf:
			return 0
		return func(node)
	return inner


class Node:
	def __init__(self, key):
		self.left = self.right = AVL.leaf
		self.key = key
		self.size = 1
		self.height = 1


class AVL(object):
	leaf = None

	def __init__(self):
		self.root = AVL.leaf

	@staticmethod
	@zeroleaf
	def calculate_size(node):
		return 1 + AVL.get_size(node.left) + AVL.get_size(node.right)

	
	@staticmethod
	@zeroleaf
	def calculate_height(node):
		return 1 + max(AVL.get_height(node.left), AVL.get_height(node.right))
	
	@staticmethod
	def recalculate(node):
		node.height = AVL.calculate_height(node)
		node.size = AVL.calculate_size(node)

	@staticmethod
	@zeroleaf
	def get_size(node):
		return node.size

	@staticmethod
	@zeroleaf
	def get_height(node):
		return node.height
	
	@staticmethod
	@zeroleaf
	def get_balance(node):
		return  AVL.get_height(node.right) - AVL.get_height(node.left)

	@staticmethod
	def _insert(node, key, index = 0):
		if node is AVL.leaf:
			return Node(key)

		leftsize = AVL.get_size(node.left)
		if index <= leftsize:
			node.left = AVL._insert(node.left, key, index)
		else:
			node.right = AVL._insert(node.right, key, index - leftsize - 1)

		AVL.recalculate(node)
		balance = AVL.get_balance(node)
		
		# rotation cases
		if balance == -2:
			if AVL.get_balance(node.left) == +1:
				node.left = AVL.rotate_left(node.left)
			return AVL.rotate_right(node)

		if balance == +2:
			if AVL.get_balance(node.right) == -1:
				node.right = AVL.rotate_right(node.right)
			return AVL.rotate_left(node)
		return node

	@staticmethod
	def rotate_left(node):			
		R = node.right
		LR = R.left
		R.left, node.right = node, LR
		AVL.recalculate(node)
		AVL.recalculate(R)
		return R

	@staticmethod
	def rotate_right(node):
		L = node.left
		LR = L.right
		L.right, node.left = node, LR
		AVL.recalculate(node)
		AVL.recalculate(L)
		return L


class AVList(AVL):
	def __init__(self, *initializers):
		super().__init__()
		for key in initializers:
			self.append(key)

	def insert(self, index, key):
		self.root = AVL._insert(self.root, key, index = index)

	def append(self, key):
		self.insert(AVL.get_size(self.root) + 1, key)

	def __repr__(self):
		nodes = []
		def trv(node):
			if not node: return
			trv(node.left)
			nodes.append(node.key)
			trv(node.right)
		trv(self.root)
		return str(nodes)


if __name__ == "__main__":
	avl = AVList(10, 20, 30, 40, 50, 25)
	for i in range(1, 10, 2):
		avl.insert(i, "$")
	print( avl )


