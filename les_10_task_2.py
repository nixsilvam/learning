def palindrom():
    word = str(input())
    word = word.replace(' ', '')  # А РОЗА УПАЛА НА ЛАПУ АЗОРА
    a = word[::-1]
    if word == a:
        return True
    else:
        return False


print(palindrom())
