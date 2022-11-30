def f(a):
    result = ''
    while a != 0:
        result = str(a % 9) + result
        a //= 9
    return result


count = 0
for i in range(6561, 59049):
    row = f(i)
    if int(row[0]) % 2 == 0 and not(row[-1] in ["1", "8"]) and row.count("3") <= 1:
        count += 1
print(count)
