n = int(input())
file = open("input.txt")
W = []
for i in range(n):
    data = [int(x) for x in file.readline().split()]
    W.append(data)
active = [True] * n
R = W[0][:]
P = [0] * n
active[0] = False
P[0] = -1
for i in range(n - 1):
    minDist = 1e10
    for j in range(n):
        if active[j] and R[j] < minDist:
            minDist = R[j]
            kMin = j
    active[kMin] = False
    for j in range(n):
        if R[kMin] + W[kMin][j] < R[j]:
            R[j] = R[kMin] + W[kMin][j]
            P[j] = kMin
i = n - 1
while i >= 0:
    print(i, end="")
    i = P[i]
