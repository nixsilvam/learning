def user_input():
    lines = []
    while True:
        i = input()
        lines.append(i)
        if not i:
            break
    return lines


def file_write(lines):
    with open('test.txt', "w+") as file:
        file.writelines("%s\n" % line for line in lines)


file_write(user_input())
