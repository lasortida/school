for x in range(79, -1, -1):
    number1 = 75 + 80 * x + (3 * (80 ** 2))
    number2 = x * 80 + 14 * (80 ** 2)
    if (number1 + number2) % 17 == 0:
        print((number1 + number2) / 17)
        break
        