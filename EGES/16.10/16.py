def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n - 1) - 1


a = 1000 * (999 * f(998) - 1) - 1
b = f(997)
print(a / b)
