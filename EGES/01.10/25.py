data = []

for m in range(2, 30, 2):
    for n in range(1, 30, 2):
        n = 2 ** m * 3 ** n
        if 400000000 <= n <= 600000000:
            data.append(n)

data.sort()
print(data)