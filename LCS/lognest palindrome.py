# Function to find the length of the longest palindromic subsequence
# of substring `X[i…j]`
def longestPalindrome(X, i, j):
 
    # Base condition
    if i > j:
        return 0
 
    # If the string `X` has only one character, it is a palindrome
    if i == j:
        return 1
 
    # If the last character of the string is the same as the first character
    if X[i] == X[j]:
        # include the first and last characters in palindrome
        # and recur for the remaining substring `X[i+1, j-1]`
        return longestPalindrome(X, i + 1, j - 1) + 2
 
    '''
      If the last character of the string is different from the first character
        1. Remove the last character and recur for the remaining substring
           `X[i, j-1]`
        2. Remove the first character and recur for the remaining substring
           `X[i+1, j]`
    '''
 
    # Return the maximum of the two values
    return max(longestPalindrome(X, i, j - 1), longestPalindrome(X, i + 1, j))


from numpy import zeros
def longestPalindrome2(X):
	X = list(X)
	Y = list(reversed(X))
	X.insert(0, " ")
	Y.insert(0, " ")
	n = len(X)

	T = zeros( (n, n) )
	for x in range(1, n):
		for y in range(1, n):
			
			if X[x] == Y[y]:
				T[x][y] = T[x-1][y-1] + 1
			else:
				T[x][y] = max(T[x][y-1], T[x-1][y])
	
	return T[n-1][n-1]


from random import sample
alfa = "asdf"*10
for i in range(10000):
	word = sample(alfa, 4)
	try:
		assert( longestPalindrome2(word) == longestPalindrome(word, 0, len(word)-1) )
	except AssertionError:
		print(word)
		print(longestPalindrome2(word), longestPalindrome(word, 0, len(word)-1))
		break


