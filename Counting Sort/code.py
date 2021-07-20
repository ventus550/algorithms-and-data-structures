data = [0, 2, 1, 8, 4, 3, 2, 1, 10]

def counting_sort(array):
	n = len(array)
	u = 11
	
	# assume all the elements belong to the {0,1,2,3,4,5,6,7,8,9,10} universe
	counted = [0]*u
	for x in array:
		counted[x] += 1
	
	# transform counted into array of sums
	for i in range(1, u):
		counted[i] += counted[i-1]
	
	# actual sorting
	res = [0]*n

	print(counted)
	for i in range(u-1, 0, -1):

		while counted[i] != counted[i-1]:
			res[counted[i]-1] = i
			counted[i] -= 1
	
	return res

print(counting_sort(data))