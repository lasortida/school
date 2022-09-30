file = open("26.txt")
n = int(file.readline())
data = [int(x) for x in file.readlines()]
data.sort(reverse=True)
count = 0
presents = []
previous = 100000
for i in range(len(data)):
    if previous - data[i] >= 3:
        presents.append(data[i])
        previous = data[i]
        count += 1
print(count)
print(presents[-1])