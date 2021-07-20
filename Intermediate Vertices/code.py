
Tree = [
	[],
	[2, 3, 4],
	[5, 6, 7],
	[8, 9],
	[10],
	[],
	[],
	[11, 12],
	[],
	[13, 14]
]

def solve(tree, seq):

	timer = 0
	def DFS(v):
		nonlocal timer

		
		