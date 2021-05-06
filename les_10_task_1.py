def file_write():
    f = open('test.txt', "w+", encoding='UTF-8')
    while True:
        i = input()
        f.write(i + '\n')
        if not i:
            break
    f.close()


file_write()
