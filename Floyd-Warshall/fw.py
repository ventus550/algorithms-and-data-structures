from itertools import product
from numpy import array, fill_diagonal, inf

# adjacency matrix representation of a graph
# we mark missing edges with zeros
data = [
    #0  1  2  3  4  5
	[0, 7, 1, 0, 0, 0], #0
	[7, 0, 0, 2, 8, 0], #1
	[1, 0, 0, 6, 0, 0], #2
	[0, 2, 6, 0, 5, 3], #3
	[0, 8, 0, 5, 0, 4], #4
	[0, 0, 0, 3, 4, 0], #5
]

def FW(graph):
	n = len(graph)
	dp = array(graph, dtype=float)
	dp[dp == 0] = inf
	fill_diagonal(dp, 0)

	for k, i, j in product(range(n), range(n), range(n)):
		alt = dp[i, k] + dp[k, j]
		if alt < dp[i, j]:
			dp[i, j] = alt
	return dp

print(FW(data))