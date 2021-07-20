from math import inf

data = [
	(0, 9), (5, 6), (1, 3), (3, 9),
	(3, 4), (3, 5), (7, 9), (2, 3),
	(1, 5), (2, 4), (4, 8), (5, 9)
]

def solve(sections):
	# sort sections with respect to their right coordinate
	ordered = sorted(sections, key=lambda x:x[1])

	res = set()
	most_right = -inf
	for s in ordered:
		if s[0] > most_right:
			most_right = s[0]
			res.add(s)
	return res

print(solve(data))