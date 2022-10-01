row = "9" * 65
while "999" in row or "222" in row:
    if "222" in row:
        row = row.replace("222", "9", 1)
    else:
        row = row.replace("999", "2", 1)
i = 0
summa = 0
while i < len(row):
    summa += int(row[i])
    i += 1
print(summa)
print(row)
