from datetime import date


def is_date(y, m, d):
    try:
        date(y, m, d)
        return True
    except ValueError:
        return False


# Возможное использование функции:

# ye = int(input('Enter the year: '))
# mo = int(input('Enter the month: '))
# day = int(input('Enter the day: '))
# print(is_date(ye, mo, day))

# print(is_date(2020, 2, 29))
# print(is_date(2007, 2, 29))
