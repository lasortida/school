import math

H, S, V = map(int, input().split())

i = 0.30
minimal = H
save = 0
while i <= 0.5:
    a = i * math.pi
    t = S / (V * math.cos(a))
    y = V * t * math.sin(a) - ((9.8 * (t ** 2)) / 2)
    if abs(y - H) < minimal:
        minimal = abs(y - H)
        save = a
    i += 0.01
print(int((save * 180) / math.pi))
