def f(n):
    if 1 <= n <= 3:
        return 1
    else:
        return f(n - 3) + f(n - 2)


print(f(10))
