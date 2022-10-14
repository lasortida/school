L = 1000  # постоянные
K = 0.5

N = 1
W = 0
day = 0
statistic = [1]
queue_index = 0
while N > 0:
    Z = K * ((L - N - W) / L) * N
    statistic.append(Z)
    if day <= 5:
        V = 0
    else:
        V = statistic[queue_index]
        queue_index += 1
    W = W + V
    N = N + Z - V
    day += 1
    print(N, Z, W)

print(day)
