data = [3, 2, 0, 8, 15, 3, 2, 1, 10]

def min_max(array):
	n = len(array)
	mx = set(); mn = set()

	for i in range(n+1 // 2):
		a,b = array[i], array[n - i - 1]
		print(a,b)

		if a < b:
			mx.add(b); mn.add(a)
		else:
			mx.add(a); mn.add(b)
	
	return (max(mx), min(mn))

print(min_max(data))

		