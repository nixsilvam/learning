import copy


def shift(spsk, stp):
    copy_list = copy.deepcopy(spsk)
    if stp < 0:
        stp = abs(stp)
        for n in range(stp):
            copy_list.append(spsk.pop(0))
    else:
        for n in range(stp):
            copy_list.insert(0, spsk.pop())


lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst)

# shift(lst, -5)
# print(lst)

# shift(lst, 3)
# print(lst)

inp = int(input('Insert steps of the shift: '))
shift(lst, inp)
print(lst)
