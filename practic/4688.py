file = open("test.txt")
n = int(file.readline())
dict = {}
count = 0
for item in file.readlines():
    building, entrance = item.split()
    entrance = int(entrance)
    if building in dict.keys():
        dict[building].append(entrance)
    else:
        b = [entrance]
        dict[building] = b
for key in dict.keys():
    dict[key].sort()
    last_entrance = dict[key][-1]
    for i in range(1, last_entrance + 1):
        if i in dict[key]:
            pass
        else:
            right = i + 3
            left = i - 3
            if right > last_entrance:
                right = last_entrance
            if left < 1:
                left = 1
            neighbours = 0
            for j in range(i, right + 1):
                if j in dict[key]:
                    neighbours += 1
                else:
                    break
            for j in range(i, left - 1, -1):
                if j in dict[key]:
                    neighbours += 1
                else:
                    break
            if neighbours >= 3:
                count += 1
print(count)
