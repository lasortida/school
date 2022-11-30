file = open("17.txt")
data = [int(x) for x in file.readlines()]
min_val = min(data)
count = 0
max_result = 0
for i in range(len(data) - 1):
    first_val = data[i]
    second_val = data[i + 1]
    if first_val % 117 == min_val or second_val % 117 == min_val:
        count += 1
        if first_val + second_val > max_result:
            max_result = first_val + second_val
print(count)
print(max_result)
