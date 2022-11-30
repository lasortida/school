row = ">" + ("1" * 25) + ("2" * 17) + ("3" * 10)
while ">1" in row or ">2" in row or ">3" in row:
    if ">1" in row:
        row = row.replace(">1", "22>3", 1)
    if ">2" in row:
        row = row.replace(">2", "2>", 1)
    if ">3" in row:
        row = row.replace(">3", "11>2", 1)
print(row.count("2") * 2 + row.count("1") + row.count("3") * 3)