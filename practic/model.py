# Нужен файл, куда записываются данные!


import matplotlib.pyplot as plt

L = 1000  # постоянные
K = 0.5

N = 1
W = 0
day = 0
statistic = [1]
queue_index = 0

N_values = [1]
W_values = [0]

file = open("answer.txt", "w")
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
    N_values.append(N)
    W_values.append(W)
    day += 1
    file.write(f"День {day}. Всего заболевших - {N}. Всего выздоровело - {W}. \n")
    if day == 100:
        break

days = [i for i in range(0, 101)]

fig, ax = plt.subplots()

ax.plot(days, N_values, label="Количество заболевших")
ax.plot(days, W_values, label="Количество переболевших")

ax.legend()

plt.title("Модель эпидемии гриппа")
plt.xlabel("День")
plt.ylabel("Кол-во человек")
plt.grid()
plt.show()

file.close()
