from heap import MinHeap

def heap_sort(array):
	H = MinHeap(array)
	res = [ H.pop() for _ in range(len(array))]
	return res

print(heap_sort([0, 2, 5, 1, 7, 3, 4, 1, 3, 8, 5, 8, 8, 3]))