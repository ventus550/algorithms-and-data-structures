
Tree = [
	[1, 2, 3],  #0
	[4, 5, 6],	#1
	[7, 8],		#2
	[9],		#3
	[],			#4
	[],			#5
	[10, 11],	#6
	[],			#7
	[12, 13],	#8
	[],			#9
	[],			#10
	[],			#11
	[],			#12
	[],			#13
]

Seq = [ (0, 0), (1, 2), (1, 10), (10, 1) ] 

def solve(tree, seq):
	n = len(tree)
	enter_time = [None] * n
	leave_time = [None] * n

	timer = 0
	def DFS(v):
		nonlocal timer

		enter_time[v] = timer

		for child in tree[v]:
			timer += 1
			DFS(child)
		
		leave_time[v] = timer
	
	def is_intermidiate(v, u):
		A, B = enter_time[v], leave_time[v]
		a, b = enter_time[u], leave_time[u]
		return A <= a and b <= B
	
	DFS(0)
	return [is_intermidiate(v, u) for v, u in seq]

print(solve(Tree, Seq))