data = [0, 2, 1, 8, 4, 3, 2, 1, 10]

def insert_sort(array):
	n = len(array)
	for i in range(1, n):
		j = i
		while array[j-1] > array[j] and j > 0:
			array[j], array[j-1] = array[j-1], array[j]
			j -= 1
	return array

print(insert_sort(data))