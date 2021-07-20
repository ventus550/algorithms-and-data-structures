a, b = 4096, 256

def GCD(A, B):
    if A == 0:
        return B, 0, 1

    gcd, x1, y1 = GCD(B%A, A)
    x = y1 - (B//A) * x1
    y = x1

    return gcd, x, y