import copy


def shift(spsk, stp):
    copy_list = copy.deepcopy(spsk)
    if stp < 0:
        stp = abs(stp)
        for n in range(stp):
            copy_list.append(copy_list.pop(0))
    else:
        for n in range(stp):
            copy_list.insert(0, copy_list.pop())
    return copy_list


lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst)

# shift(lst, -5)
# print(lst)

# shift(lst, 3)
# print(lst)

inp = int(input('Insert steps of the shift: '))
shift(lst, inp)
print(lst)
