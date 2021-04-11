def triangle(a, b):
    s1 = a / 2 * b
    return s1


def square(a):
    s2 = a ** 2
    return s2


x = int(input('Введите сторону фигуры: '))
fig_type = input('Введите тип фигуры (треугольник или квадрат): ')
if fig_type == 'квадрат' or fig_type == 'square':
    print(square(x))
else:
    y = int(input('Введите другую сторону фигуры: '))
    print(triangle(x, y))
