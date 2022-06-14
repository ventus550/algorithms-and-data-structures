from math import ceil

def F(a, b):
    res = []

    while a != 0:
        c = ceil(b / a)
        a = a*c - b
        b = b*c

        res.append(c)
           
    return res

print(F(733, 4692)) # note that the optimal solution is {12, 23, 34}