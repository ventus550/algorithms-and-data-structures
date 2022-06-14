def LCIS(arr1, arr2):
	n = len(arr1); m = len(arr2)

	# table[j] is going to store length of LCIS
	# ending with arr2[j]. We initialize it as 0,
	table = [0] * m

	# Traverse all elements of arr1[]
	for i in range(n):

		# Initialize current length of LCIS
		current = 0

		# For each element of arr1[],
		# traverse all elements of arr2[].
		for j in range(m):

			# If both the arrays have same elements.
			# Note that we don't break the loop here.
			if (arr1[i] == arr2[j]):
				table[j] = max(current + 1, table[j])

			# Now seek for previous smaller common
			# element for current element of arr1
			if (arr1[i] > arr2[j]):
				current = max(current, table[j])

	# The maximum value in table[]
	# is out result
	return table

print(LCIS([5,5,1],[5,5,1]))
