select = [i for i in range(24200000, 24200171)]
count = 0
a = set()
for x in range(100, 250):
    for z in range(10000, 100000):
        if (100001 * x) + (101 * z) in select:
            a.add((100001 * x) + (101 * z))
print(len(a))
