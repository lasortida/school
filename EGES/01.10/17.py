# file = open("17.txt")
# count = 0
# max_pair = 0
# data = [int(x) for x in file.readlines()]
# for i in range(len(data) - 1):
#     first_num = data[i]
#     second_num = data[i + 1]
#     if (first_num * second_num) % 62 == 0:
#         count += 1
#         if first_num + second_num > max_pair:
#             max_pair = first_num + second_num
# print(count)
# print(max_pair)

count = m = 0
f = open('17.txt')
l = [int(i) for i in f]
for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if l[i] * l[j] % 62 == 0:
            count += 1
            m = max(m, l[i] + l[j])
print(count, m)
