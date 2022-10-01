file = open("28138.txt")
s, n = map(int, file.readline().split())
data = [int(x) for x in file.readlines()]
data.sort()
total = 0
count = 0
for i in range(len(data)):
    if total + data[i] <= s:
        total += data[i]
        count += 1
    else:
        break
delta = s - total
max_el = 0
for i in data[count:]:
    if i <= delta + data[count - 1]:
        max_el = i
print(count)
print(max_el)