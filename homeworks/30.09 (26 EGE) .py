file = open("26-j6.txt")
n = int(file.readline())
data = [int(x) for x in file.readlines()]
data.sort()
s = sum(data) * 0.9
i = 0
count = 0
while i < len(data):
    if sum(data[:i + 1]) + sum(data[i + 1:]) * 0.8 <= s:
        count += 1
    else:
        break
    i += 1
max_file = 0
j = count
while j < len(data):
    if sum(data[:count - 2]) + data[count - 1] * 0.8 + data[j] + sum(data[j + 1: ]) * 0.8 <= s:
        max_file = data[j]
    else:
        break
    j += 1
print(count)
print(max_file)
