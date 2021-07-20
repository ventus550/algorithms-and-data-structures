from random import randint

data = [0, 2, 1, 8, 4, 3, 2, 1, 10]



# take first element as pivot
def deterministic_random(array, left, right):
	pass

# take random pivot
def random(array, left, right):
	p = randint(left, right)
	array[left], array[p] = array[p], array[left]

def quicksort(array, choosepivot=random):
	small = 3

	# we can speed up the algortithm by sorting tiny subarrays in O(n^2) time
	def insert_sort(array, left, right):
		for i in range(left+1, right):
			j = i
			while array[j-1] > array[j] and j > left:
				array[j], array[j-1] = array[j-1], array[j]
				j -= 1

	def partition(left, right):
		p = array[left] # pivot
		i = left; j = right
		
		while i < j:

			while array[j] >= p and j > left:
				j -= 1

			while array[i] < p:
				i += 1

			if i < j:
				array[i], array[j] = array[j], array[i]
			else:
				return j

	def qs(left, right):
		if right - left <= small:
			insert_sort(array, left, right+1)
		else:
			choosepivot(array, left, right)
			sep = partition(left, right)
			qs(left, sep)
			qs(sep+1, right)

	qs(0, len(array)-1)
	return array

print(quicksort(data))
