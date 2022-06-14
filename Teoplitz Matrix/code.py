

data = [
	[1, 2, 3, 4, 5],
	[6, 1, 2, 3, 4],
	[7, 6, 1, 2, 3],
	[8, 7, 6, 1, 2],
	[9, 8, 7, 6, 1]
]

def teoplitalize(matrix):
	n = len(matrix)
	return [matrix[i][0] for i in range(n-1, 0, -1)] + matrix[0]

class Teo:

	def __init__(self, tlist):
		self.n = (len(tlist) + 1) // 2
		self.diagonals = tlist

	def __getitem__(self, pos):
		i, j = pos
		return self.diagonals[j - i - 1 + self.n]
	
	def __repr__(self):
		r = range(self.n)
		return '\n'.join([ str([self[i, j] for j in r]) for i in r ])

	def __add__(self, other):
		return Teo([ self.diagonals[i] + other.diagonals[i] for i in range(2*self.n - 1) ])


t = Teo(teoplitalize(data))
print(t+t)