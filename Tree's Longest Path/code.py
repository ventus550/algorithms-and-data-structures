Tree = [
	[1, 2],
	[3, 4], [],
	[5, 6], [7, 8],
	[], [], [], [9, 10],
	[], []
]


# Find the longest path in a binary tree
def solve(tree):

	dist = 0
	def h(v):
		nonlocal dist

		children = tree[v]
		if len(children) == 0:
			return 1

		hleft = h(children[0])
		hright = h(children[1])
		
		dist = max(dist, hleft + hright + 1)
		return max(hleft, hright) + 1
	
	h(0)
	return dist


print(solve(Tree))