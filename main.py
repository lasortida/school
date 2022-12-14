row = input()
data = row.split(" ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
stack = []
let = set()
map = {}
for el in data:
    if el in alphabet:
        let.add(el)
count = len(let)
for i in range(count):
    string = input()
    a = string.split("=")
    map[a[0]] = a[1]
print(map)
for el in row:
    if el in alphabet:
        number = map[el]
        stack.append(number)
    if type(el) == int:
        let.add(int(el))
    else:
        if el in "+-*/":
            if len(stack) > 1:
                c = stack.pop()
                d = stack.pop()
                if el == "+":
                    stack.append(c + d)
                elif el == "-":
                    stack.append(d - c)
                elif el == "*":
                    stack.append(c * d)
                else:
                    stack.append(d / c)
        else:


