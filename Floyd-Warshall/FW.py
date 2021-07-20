from heapq import *
from math import inf

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
	n = len(data)
	dp = [ [x if x != 0 else inf for x in row] for row in data ]
	for v in range(n):
		dp[v][v] = 0

	for k in range(n):
		for i in range(n):
			for j in range(n):
				alt = dp[i][k] + dp[k][j]
				if alt < dp[i][j]:
					dp[i][j] = alt

	return dp

print("\n".join( [str(x) for x in FW(data)] ))