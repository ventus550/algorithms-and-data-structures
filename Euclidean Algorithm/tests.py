import alternative, extended, regular
from timeit import timeit
from random import randint
import matplotlib.pyplot as plt

D = [{}, {}, {}]

def sample():
	A = randint(0, 1000000)
	B = randint(0, 1000000)

	X = A+B
	D[0][X] = timeit(lambda : alternative.GCD(A,B), number=100)
	D[1][X] = timeit(lambda : extended.GCD(A,B), number=100)
	D[2][X] = timeit(lambda : regular.GCD(A,B),  number=100)

def xf(D):
	L = sorted(D.items())
	plt.plot([x[0] for x in L], [x[1] for x in L])

for i in range(100):
	sample()

xf(D[0])
xf(D[1])
xf(D[2])
plt.show()