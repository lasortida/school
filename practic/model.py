import math

r = 0.033
m = 0.15
v = 20
delta = 0.1

t = 0
y = 0
C = 0.4

ro = 0
h = 0

while y >= 0:
    F = -ro * abs(v) * v * C * (math.pi * r ** 2) / 2
    a = -9.8 + F/m
    y = y + v * delta + a * delta * delta / 2
    v = v + a * delta
    t = t + delta
    if y > h:
        h = y

print(t)
print(h)
print(v)

print(" ")
print(" ")

t = 2 * v / 9.8
h = (20 ** 2) / 9.8
v = -20

print(t)
print(h)
print(v)

