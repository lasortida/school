from func import isSimple, simpleArrayFromRange
import time
from matplotlib.pyplot import plot as plt

N = int(input())
result = []
start_time = time.time()
for i in range(2, N + 1):
    if isSimple(i):
        result.append(i)
print(result)
print("Перебор", "Время выполнения - ", time.time() * 1000 - start_time * 1000)
print("")
start_time = time.time()
print(simpleArrayFromRange(N))
print("Решето Эратосфена", "Время выполнения - ", time.time() * 1000 - start_time * 1000)

A = []
B = []
C = [i for i in range(1, 100000)]
for i in C:
    start_time = time.time() * 1000
    result = []
    for j in range(2, N + 1):
        if isSimple(j):
            result.append(j)
    end_time = time.time() * 1000
    A.append(end_time - start_time)
for i in C:
    start_time = time.time() * 1000
    result = simpleArrayFromRange(i)
    end_time = time.time() * 1000
    B.append(end_time - start_time)
plt.plot(A, C)
plt.plot(B, C)
plt.grid()
plt.sh