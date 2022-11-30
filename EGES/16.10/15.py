def f(n, m):
    return n % m == 0


for A in range(1, 100000):
    ok = True
    for x in range(1, 10000):
        if not((f(x, 6) <= (not f(x, 10))) or (x + A > 121)):
            ok = False
            break
    if ok:
        print(A)
        break
