def isSimple(a):
    if a > 1:
        k = 2
        while k <= int(a ** 0.5):
            if a % k == 0:
                return False
            k += 1
        return True
    else:
        return False

def simpleArrayFromRange(n):
    A = [True] * (n + 1)
    k = 2
    while k * k <= n:
        if A[k]:
            i = k * k
            while i <= n:
                A[i] = False
                i += k
        k += 1
    result = [i for i in range(2, n + 1) if A[i]]
    return result
