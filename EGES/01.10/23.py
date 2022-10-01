def trener(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    else:
        return trener(start + 1, end) + trener(start + 2, end)


print(trener(1, 11))
