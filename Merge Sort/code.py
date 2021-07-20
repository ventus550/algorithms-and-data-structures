from math import inf

data = [0, 2, 1, 8, 4, 3, 2, 1, 10]

def merge_sort(array):
	length = len(array)

	if length == 1:
		return array

	# add infinities to simplify branching
	L = merge_sort(array[ :length//2 ]) + [inf]
	R = merge_sort(array[ length//2: ]) + [inf]
	A = []

	l = r = 0
	while l + r != length:
		
		if L[l] < R[r]:
			A.append( L[l] )
			l += 1
		else:
			A.append( R[r] )
			r += 1

	return A
