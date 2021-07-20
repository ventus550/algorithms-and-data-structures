from random import randint


def GCD(A, B):
    
    if A < B:
        A, B = B, A

    if A == 0:
        return B
    if B == 0:
        return A

    if A % 2 == B % 2 == 0:
        return 2 * GCD(A // 2, B // 2)
    
    if A % 2 == B % 2 == 1:
        return GCD( (A - B)//2, B )

    if A % 2 != 0 and B % 2 == 0:
        return GCD(A, B // 2)
    
    if A % 2 == 0 and B % 2 != 0:
        return GCD(A // 2, B)
