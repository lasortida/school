import csv

file = open("107_9.csv")
reader = csv.reader(file, delimiter=";")
count = 0
for row in reader:
    data = [int(item) for item in row]
    min_num = min(data)
    max_num = max(data)
    data.remove(min_num)
    data.remove(max_num)
    a = 0
    for el in data:
        a += el ** 2
    if (min_num + max_num) ** 2 > a:
        count += 1
print(count)
