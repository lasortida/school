# print("x y z w")
#
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if not((w <= (y == z)) and (y == (z <= x))):
#                     print(x, y, z, w, sep="-")

# for N in range(1, 100000000):
#     a = bin(N)[2:]
#     b = ""
#     for el in a:
#         if el == "1":
#             b += "0"
#         else:
#             b += "1"
#     c = int(b, 2)
#     if N - c == 979:
#         print(N)
#         break


count = 0
for i in range(59049, 531441):
    print(i)
    print(" ")
    count_n = 0
    count_4 = 0
    while i > 0:
        a = i % 9
        if a == 4:
            count_4 += 1
            if count_4 > 1:
                break
        if a % 2 != 0:
            count_n += 1
            if count_n > 3:
                break
        i //= 9
    if count_4 == 1 and count_n == 2:
        count += 1
print(count)