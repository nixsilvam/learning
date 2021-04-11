def les_5_task_2(n):
    words = len(n.split())
    return len(n), words


x = str(input('Введите строку: '))
print('Количество символов, слов: ', les_5_task_2(x))

