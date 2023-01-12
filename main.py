def f(n):
    row = bin(n)[2:]
    if row.count("1") % 2 == 0:
        row = "1" + row
        row = row[:-2] + "01"
    else:
        row += "10"
        row = "1" + row[2:]
    return int(row, 2)


maxel = 0
for i in range(10000):
    a = f(i)
    if (a > maxel and a <= 100):
        maxel = a
print(maxel)