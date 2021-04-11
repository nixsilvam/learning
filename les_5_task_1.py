from math import sqrt


def is_prime(numb):
    if numb % 2 == 0 and numb != 2:
        return False
    if numb == 0 or numb == 1:
        return False
    for x in range(3, int(sqrt(numb).real) + 1, 2):
        if numb % x == 0:
            return False
    return True


y = int(input('Введите число от 1 до 1000:'))
print(is_prime(y))
