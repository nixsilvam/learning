def palindrom():
    word = str(input())
    word = word.replace(' ', '')  # А РОЗА УПАЛА НА ЛАПУ АЗОРА
    a = word[::-1]
    if word == a:
        print(True)
    else:
        print(False)


palindrom()
