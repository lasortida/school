file = open("zadanie24_2.txt")
row = file.readline()
cur_count = 0
max_len = 0
for el in row:
    if el == "D":
        cur_count += 1
    else:
        if cur_count > 0:
            if cur_count > max_len:
                max_len = cur_count
            cur_count = 0
print(max_len)
