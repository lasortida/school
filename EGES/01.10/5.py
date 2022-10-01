def get_result(n):
    binary = bin(n)[2:]
    i = binary.find("1")
    j = i + 1
    while j < len(binary) and binary[j] == "0":
        j += 1
    if i == 0 and j == len(binary):
        result_row = "0"
    elif j == len(binary):
        result_row = binary[:i]
    else:
        result_row = binary[:i] + binary[j:]
    result = int(result_row, 2)
    return n - result


data = []
for i in range(100, 3001):
    data.append(get_result(i))
data = set(data)
print(len(data))
