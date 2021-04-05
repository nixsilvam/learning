s = list()
len = 0
prod = 1
sum = 0
even = 0
odd = 0
while (x := abs(int(input('Введите целое неотрицательное число: ')))) != 0:
    s.append(x)
    len += 1
for y in s:
    prod *= y
    sum += y
    if y % 2 == 0:
        even += 1
    else:
        odd += 1
max_s = max(s)
count_max = s.count(max(s))
s_s = sorted(set(s))
s_s.pop()
print('Количество введённых чисел:', len)
print('Произведение введённых чисел:', prod)
print('Сумма введённых чисел:', sum)
print('Среднее арифметическое:', int(sum / len))
print('Значение наибольшего элемента последовательности:', max_s, '''
                                       Порядковый номер:''', s.index(max_s) + 1)
print('Количество чётных элементов:', even, '''
                          Нечётных:''', odd)
print('Значение второго по величине элемента:', max(s_s))
print('Количество элементов последовательности, равных её наибольшему значению:', count_max)
