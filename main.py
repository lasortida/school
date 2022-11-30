# def f(n, m):
#     return n % m == 0
#
#
# for A in range(-1000, 100000):
#     ok = True
#     for x in range(1, 10000):
#         if not((f(72, x) <= (not (f(120, x)))) or (A - x > 100)):
#             ok = False
#             break
#     if ok:
#         print(A)
#         break


# def f(n):
#     if n == 0:
#         return 0
#     else:
#         return f(n - 1) + n
#
#
# print((1134567004 - 237567892 + 1) // 3)


file = open("17.txt")
data = [int(x) for x in file.readlines()]
mini = 10000
for el in data:
    if str(el)[-1] == "7" and el < mini:
        mini = el
count = 0
maxi = 0
for i in range(len(data) - 1):
    first = data[i]
    second = data[i + 1]
    row = str(first)[-1] + str(second)[-1]
    if row.count("7") == 1 and (first ** 2 + second ** 2) < mini ** 2:
        count += 1
        if first ** 2 + second ** 2 > maxi:
            maxi = first ** 2 + second ** 2
print(count)
print(maxi)