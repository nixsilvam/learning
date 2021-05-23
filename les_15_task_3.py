import re


def again():             # хз зачем, не уверена, что это сильно сократило количество напечатанных мною символов
    return 'Try again:'


def password_check():
    up = re.compile(r'[A-Z]')
    low = re.compile(r'[a-z]')
    digit = re.compile(r'(\d)')
    spec = re.compile(r'[-$#@+=]')
    len8 = re.compile(r'\S{8,}')
    while True:
        pw = input()
        if low.search(pw) is None:
            print('The entered password doesn\'t have any lower case letter')
            print(again())
            continue
        if up.search(pw) is None:
            print('The entered password doesn\'t have any upper case letter')
            print(again())
            continue
        if digit.search(pw) is None:
            print('The entered password doesn\'t have any digit')
            print(again())
            continue
        if spec.search(pw) is None:
            print('The entered password doesn\'t have any specials symbols like - $ # @ + =')
            print(again())
            continue
        if len8.search(pw) is None:
            print('The entered password should have atleast 8 characters and no space in between')
            print(again())
        else:
            print('Password is correct')
            return pw


if __name__ == '__main__':
    print('Please enter a new password: ')
    password_check()
