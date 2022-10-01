for x in range(1, 10000):
    ok = False
    for s in range(1, 10000):
        save = s
        s = 100 * s + x
        n = 1
        while s < 2021:
            s += 5 * n
            n += 1
        if n == 17:
            print(x)
            print(save)
            ok = True
            break
    if ok:
        break
