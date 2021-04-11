some_list = [int(input('Введите целое число: ')) for i in range(10)]
# предположим, в списке 10 элементов
for x in some_list:
    if some_list[x] // 2 != 0:
        some_list[x] = 0
print(some_list)
print(some_list.count(0))
