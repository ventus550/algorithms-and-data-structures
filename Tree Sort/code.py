data = [1, 3, 4, 5, 0, 7, 2, 3, 8, 1, 1, 1, 1, 1, 4, 2, 1, 4, 1, 2, 1, 1, 1]

class Node(int):

	def __init__(self, val):
		self.left, self.right = None, None
		self.val = val
		self.count = 1


class Tree:

	def __init__(self):
		self.root = None
	
	def __getitem__(self, item):
		child = p = self.root
		while child:
			aux = child

			if p >= item:
				child = p.left 
			else:
				child = p.right

			p = aux
		return p
	
	def insert(self, key):
		match = self[key]

		if key < match:
			match.left = Node(key)
		elif key > match:
			match.right = Node(key)
		else:
			match.count += 1
	

def tsort(L):

	def rec(v):
		if v == None:
			return []
		return rec(v.left) + [v.val]*v.count + rec(v.right)	

	if not L:
		return []
	
	T = Tree()
	T.root = Node(L[0])

	for i in range(1, len(L)):
		T.insert(L[i])
	
	return rec(T.root)


print( tsort(data) )
	


