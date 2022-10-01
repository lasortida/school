file = open("26 (1).txt")
n = int(file.readline())
dictionary = {}
count = 0
for item in file.readlines():
    building, entrance = item.split()
    entrance = int(entrance)
    if building in dictionary.keys():
        dictionary[building].append(entrance)
    else:
        b = [entrance]
        dictionary[building] = b
max_key = 0
min_entrance = 10000000
for key in dictionary.keys():
    dictionary[key].sort()
    last_entrance = dictionary[key][-1]
    for i in range(1, last_entrance + 1):
        if i in dictionary[key]:
            pass
        else:
            right = i + 3
            left = i - 3
            if right > last_entrance:
                right = last_entrance
            if left < 1:
                left = 1
            neighbours = 0
            for j in range(i + 1, right + 1):
                if j in dictionary[key]:
                    neighbours += 1
                else:
                    break
            for j in range(i - 1, left - 1, -1):
                if j in dictionary[key]:
                    neighbours += 1
                else:
                    break
            if neighbours >= 3:
                count += 1
                if int(key) > max_key:
                    max_key = int(key)
                    min_entrance = i
                break
print(count)
print(min_entrance)
