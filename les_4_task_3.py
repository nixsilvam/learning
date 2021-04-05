a = int(input('Введите целое число:'))
b = int(input('Введите целое число:'))
if a < b:
    for x in range(a, b + 1):
        print(x)
else:
    for x in range(a, b - 1, -1):
        print(x)
