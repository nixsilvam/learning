import csv
import argparse
import os
import re


def check_args() -> list:
    if args.iata_code is not None:
        return iata_check()
    elif args.country is not None:
        return country_check()
    elif args.name is not None:
        return name_check()
    elif args.iata_code and args.country and args.name is None:
        raise Exception('NoOptionsFoundError')
    else:
        raise Exception('MultipleOptionsError')


def iata_check() -> list:
    iata = re.search(r'[A-Z]{3}', args.iata_code)
    if iata:
        iata_list = open_file(iata.group(), 'iata_code')
        if iata_list:
            return iata_list
        else:
            raise Exception('AirportNotFoundError', iata)
    else:
        raise Exception('IATACodeError', iata)


def country_check() -> list:
    country_list = open_file(args.country, 'iso_country')
    if country_list:
        return country_list
    else:
        raise Exception('CountryNotFoundError', args.country)


def name_check() -> list:
    pattern = re.compile(f'[a-dA-D]*{args.name}[a-dA-D]*')
    name_list = []
    cur_folder = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(cur_folder, 'airport-codes_csv.csv')
    with open(filename, 'r', encoding='UTF-8') as f:
        csv_reader = csv.DictReader(f, delimiter=',')
        for row in csv_reader:
            name = row['name']
            if re.search(pattern, name):
                name_list.append(row)
    if name_list:
        return name_list
    else:
        raise Exception('AirportNotFoundError', args.name)


def open_file(arg, argkey) -> list:
    result_list = []
    cur_folder = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(cur_folder, 'airport-codes_csv.csv')
    with open(filename, 'r', encoding='UTF-8') as f:
        csv_reader = csv.DictReader(f, delimiter=',')
        for row in csv_reader:
            if row[argkey] == arg:
                result_list.append(row)
        return result_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Airport...')
    parser.add_argument('--iata_code', type=str, default=None)
    parser.add_argument('--country', type=str, default=None)
    parser.add_argument('--name', type=str, default=None)
    args = parser.parse_args()
    peps = check_args()
    for x in peps:
        print(x)
