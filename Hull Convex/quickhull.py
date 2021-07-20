data = {
	(0, 3), (1, 1), (2, 2), (4, 4),
	(0, 0), (1, 2), (3, 1), (3, 3)
}


def side(A, B, p):
	return (p[1] - A[1]) * (B[0] - A[0]) - (B[1] - A[1]) * (p[0] - A[0])


def get_side(A, B, p):
	s = side(A, B ,p)
	if s == 0:
		return 0
	return 2*(s > 0) - 1


def dist(A, B, p):
	return abs(side(A, B, p))


def quickhull(points):

	def cut(A, B, cset, cside):
		subset = set([ p for p in cset if get_side(A, B, p) == cside])
		
		if not subset:
			return subset | {A, B}

		P = max(subset, key=lambda p: dist(A, B, p))
		return cut(A, P, subset, -side(A, P, B)) | cut(P, B, subset, -side(P, B, A))


	left = min(points, key=lambda x: x[0])
	right = max(points, key=lambda x: x[0])
	return cut(left, right, points, -1) | cut(left, right, points, 1)


print(quickhull(data))