

# parent: node // 2
# left child: 2*node + 1
# right child: 2*node + 2

class MinHeap:
	
	def __init__(self, L : list = []):
		self.heap = []
		self.n = 0
		for e in L:
			self.push(e)
	
	def push(self, e):
		self.heap.append(e)
		self.move_up(self.n)
		self.n += 1
	
	def pop(self):
		self.n -= 1
		if self.n == 0:
			return self.heap.pop()

		mn = self.heap[0]
		self.heap[0] = self.heap.pop()
		self.move_down(0)
		return mn
		
	def move_up(self, node):
		H = self.heap
		while node != 0 and H[node] < H[node // 2]:
			H[node], H[node // 2] = H[node // 2], H[node]
			node = node // 2
	
	def move_down(self, node):
		H = self.heap; n = self.n

		while True:
			# choose lesser child node
			child = 2*node + 1
			if child < n - 1 and H[child] > H[child + 1]: #! doesnt work for odd-sized heaps
				child += 1

			# end if node is greater than both its children
			if child >= n or H[child] >= H[node]:
				break

			H[child], H[node] = H[node], H[child]
			node = child