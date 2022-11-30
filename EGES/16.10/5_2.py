a = 28
b = bin(a)[2:]
if b.count("1") % 2 == 0:
    b = '10' + b[:-2] + '00'
else:
    b = '11' + b[:-2] + '11'
print(int(b, 2))
