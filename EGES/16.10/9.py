import csv

file = open("9.csv")
reader = csv.reader(file, delimiter=";")
count = 0
for row in reader:
    row = [int(x) for x in row]
    max_number = max(row)
    min_number = min(row)
    row.remove(min_number)
    row.remove(max_number)
    if max_number - min_number >= 50 and row[0] * row[1] <= 1000:
        count += 1
print(count)
