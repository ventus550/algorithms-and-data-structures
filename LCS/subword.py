from numpy import empty, int64	

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
	DP = empty( (N+1, n, n) )

	for i in range(N):
		fill_zeros(DP[i])
	
	LCS(X, Y, DP[0])

	for i in range(1, N):
		T = DP[i]

		for x in range(1, n):
			for y in range(1, n):

				if X[x] == Y[y] == substring[i]:

					if DP[i-1, x-1, y-1] == 0:
						T[x][y] = 0
					else:
						T[x][y] = DP[i-1][x-1][y-1] + 1
				else:
					T[x][y] = max( T[x-1][y], T[x][y-1] )

	T = DP[N]
	for x in range(1, n):
		for y in range(1, n):

			if X[x] == Y[y]:

				if DP[i-1, x-1, y-1] == 0:
					T[x][y] = 0
				else:
					T[x][y] = DP[i-1][x-1][y-1] + 1
			else:
				T[x][y] = max( T[x-1][y], T[x][y-1] )



	return DP[N][n-1][n-1]

print(solve( X, Y, substring ))
					
	



