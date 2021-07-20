data = [0, 2, 1, 8, 4, 3, 2, 1, 10]

def select_sort(array):
	for i in range(len(array)):
		for j in range(len(array)):
			if array[i] < array[j]:
				array[i], array[j] = array[j], array[i]
	return array