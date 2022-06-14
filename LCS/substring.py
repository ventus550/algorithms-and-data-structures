from numpy import empty, int64



'''
DP[i, x, y]:

	if i == 0:
		LCS

	if x != y:
		max( DP[i, x-1, y], DP[i, x, y-1] )
	
	if x == y:

		if x == "S":
			DP[i-1, x-1, y-1] + 1
		
		else:

			if DP[i, x-1, y-1] == 0:
				max?( DP[i, x-1, y], DP[i, x, y-1])

			else:
				DP[i, x-1, y-1] + 1

'''


class word(str):
	def __getitem__(self, i: int) -> str:
		return super().__getitem__(i-1)

substring = word("MATURA")
X = word("MRMAAATRAMATURMAMATURA")
Y = word("ARATURAMAARATURAMUTURA")

def fill_zeros(T):
	for i in range(len(T)):
		T[0][i] = 0
		T[i][0] = 0


def LCS(X, Y, T):
	for x in range(1, len(X)):
		for y in range(1, len(X)):
			if X[x] == Y[y]:
				T[x][y] = T[x-1, y-1] + 1
			else:
				T[x][y] = max( T[x-1][y], T[x][y-1] )


def solve(X, Y, substring):
	n = len(X)+1; N = len(substring) + 1
	DP = empty( (N, n, n) )

	for i in range(N):
		fill_zeros(DP[i])
	
	LCS(X, Y, DP[0])

	for i in range(1, N):
		T = DP[i]

		for x in range(1, n):
			for y in range(1, n):

				if X[x] == Y[y]:
					
					if X[x] == substring[i]:
						T[x][y] = DP[i-1][x-1][y-1] + 1
					elif T[x-1][y-1] == 0:
						T[x][y] = max( T[x-1][y], T[x][y-1] )
					else:
						T[x][y] = T[x-1, y-1] + 1				
				else:
					T[x][y] = max( T[x-1][y], T[x][y-1] )

	return DP[N-1][n-1][n-1]

print(solve( X, Y, substring ))
					
	



