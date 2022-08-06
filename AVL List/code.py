class Node:
	def __init__(self, key):
		self.left = self.right = AVL.leaf
		self.key = key
		self.height = 1


class AVL(object):
	leaf = None

	def __init__(self, initializers = []):
		self.root = AVL.leaf
		for key in initializers:
			self.push(key)

	def push(self, key):
		self.root = AVL.insert(self.root, key)

	def __repr__(self):
		nodes = []
		def trv(node):
			if not node: return
			trv(node.left)
			nodes.append(node.key)
			trv(node.right)
		trv(self.root)
		return str(nodes)

	@staticmethod
	def get_height(node):
		if node is AVL.leaf:
			return 0
		return node.height
	
	@staticmethod
	def calculate_height(node):
		return 1 + max(AVL.get_height(node.left), AVL.get_height(node.right))
	
	@staticmethod
	def get_balance(node):
		if node is AVL.leaf:
			return 0
		return AVL.get_height(node.left) - AVL.get_height(node.right)

	@staticmethod
	def insert(node, key):
		if node is AVL.leaf:
			return Node(key)
		elif key < node.key:
			node.left = AVL.insert(node.left, key)
		else:
			node.right = AVL.insert(node.right, key)

		node.height = AVL.calculate_height(node)
		balance = AVL.get_balance(node)
		
		# rotation cases
		if balance > 1 and key < node.left.key:
			return AVL.rotate_right(node)
		if balance < -1 and key > node.right.key:
			return AVL.rotate_left(node)
		if balance > 1 and key > node.left.key:
			node.left = AVL.rotate_left(node.left)
			return AVL.rotate_right(node)
		if balance < -1 and key < node.right.key:
			node.right = AVL.rotate_right(node.right)
			return AVL.rotate_left(node)
		return node

	@staticmethod
	def rotate_left(node):			
		R = node.right
		LR = R.left
		R.left, node.right = node, LR
		node.height = AVL.calculate_height(node)
		R.height = AVL.calculate_height(R)
		return R

	@staticmethod
	def rotate_right(node):
		L = node.left
		LR = L.right
		L.right, node.left = node, LR
		node.height = AVL.calculate_height(node)
		L.height = AVL.calculate_height(L)
		return L


if __name__ == "__main__":
	print( AVL([10, 20, 30, 40, 50, 25]) )
