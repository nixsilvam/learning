def shift(spsk, stp):
    return spsk[stp * -1:] + spsk[:stp * -1]


lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst)

# shift(lst, -5)
# print(lst)

# shift(lst, 3)
# print(lst)

inp = int(input('Insert steps of the shift: '))
print(shift(lst, inp))

