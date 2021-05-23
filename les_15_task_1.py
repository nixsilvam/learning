import csv
import re


def auto_list() -> list:
    with open('ua_auto.csv', 'r+', encoding='UTF-8') as f:
        csv_reader = csv.DictReader(f, delimiter=',')
        autolist = []
        for row in csv_reader:
            autolist.append(row)
    return autolist


def if_autonumber(user_string: str) -> bool:
    match = re.fullmatch(r'[A-CEHIKMOPTXАВСЕНІМОКРТХ]{2}\d{4}[A-CKHIАВСІКН][A-CEHIKMOPTXАВСЕНІМОКРТХ]', user_string)
    if match:
        return True
    else:
        return False


def get_region(text):
    if if_autonumber(text):
        codnumber = text[-2:]
        autolist = auto_list()
        for n in autolist:
            if n['Код 2004'] == codnumber:
                return n['Регіон'] + ' 2004г'
            if n['Код 2013'] == codnumber:
                return n['Регіон'] + ' 2013г'
    else:
        raise Exception('Error of vehicle number')
        pass


if __name__ == '__main__':
    num1 = 'ВН1010НС'
    num2 = 'АА1010АА'
    print(if_autonumber(num1))
    print(get_region(num1))
    print(if_autonumber(num2))
    print(get_region(num2))
    num3 = 'АS1010АА'
    print(if_autonumber(num3))
    print(get_region(num3))
