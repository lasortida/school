for A in range(0, 10000):
    ok = True
    for m in range(0, 10000):
        for n in range(0, 10000):
            if not((3*m + 4*n > 66) or (m <= A) or (n < A)):
                ok = False
                break
        if not ok:
            break
    if ok:
        print(A)
        break
        