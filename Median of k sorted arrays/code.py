data = [
	[2, 3, 6, 8, 10, 11],
	[1, 7, 9,11, 21, 22],
	[1, 2, 9,11, 16, 17],
	[8,12,14,16, 18, 19]
]

# def test(L):
# 	tst = []
# 	for d in data:
# 		tst += d
# 	print(sorted(tst)[len(tst) // 2])
# test(data)



def median(L):
	n = len(L[0]); k = len(L)
	begin = [0]*k; end = [n]*k
	diffs = [n]*k
	r = list(range(k))

	def midx(i):
		return (begin[i] + end[i]) // 2

	def mid(i):
		return L[i][midx(i)]
	
	def diff(i):
		if diffs[i] == 1:
			r.remove(i)
			diffs[i] = 0
		else:
			diffs[i] = end[i] - begin[i]
	
	def iterate():
		Mi = max(r, key=mid); 			M = midx(Mi)
		mi = min(reversed(r), key=mid); m = midx(mi)
		
		cut = min(m - begin[mi], end[Mi] - M)
		begin[mi] += cut; end[Mi] -= cut

		diff(mi)
		diff(Mi)

		return mid(Mi)

	
	res = None
	while r: # bad stop condtion :(
		res = iterate()
	return res
		

print(median(data))