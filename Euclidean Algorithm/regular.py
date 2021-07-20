a, b = 4096, 256

def GCD(A, B):
    if A == 0:
        return B
    return GCD(B % A, A)