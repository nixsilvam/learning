import csv
import os
import argparse
import sys


def check_args(row):
    dict_args = {k: v for k, v in args_dict.items() if v is not None}
    if not dict_args:
        sys.exit(0)
    del dict_args['o']
    map_dict = {'brand': 'BRAND',
                'color': 'COLOR',
                'year': 'MAKE_YEAR',
                'fuel': 'FUEL'}
    del dict_args['reg_num']
    result = []
    for k, v in dict_args.items():
        if row[map_dict[k]] == v:
            result.append(True)
        else:
            return False
    return all(result)


def open_file():
    result = []
    cur_folder = os.path.dirname(os.path.abspath(__file__))
    vehicles_file = os.path.join(cur_folder, args.o)
    with open(vehicles_file, 'r', encoding='UTF-8') as f:
        csv_reader = csv.DictReader(f, delimiter=';')
        for row in csv_reader:
            if check_args(row):
                result.append(row)
    return result


def file_name():
    name_dict = {k: v for k, v in args_dict.items() if v is not None}
    del name_dict['o']
    name_list = [v for v in name_dict.values()]
    if flag_regnum:
        name_list.append('regnum')
    print(name_list)
    vehicle_name = str('_'.join(name_list) + '.csv')
    print(vehicle_name)
    return vehicle_name


def save_to_file(result, namefields):
    with open(file_name(), 'w+', encoding='UTF-8') as f1:
        csv_writer = csv.DictWriter(f1, fieldnames=namefields, delimiter=',', extrasaction='ignore')
        csv_writer.writeheader()
        for row in result:
            csv_writer.writerow(row)
    print('ready')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='description...')
    parser.add_argument('o', type=str, default='tz_opendata_z01012021_po01042021.csv', nargs='?')
    parser.add_argument('--brand', type=str, help='Vehicle brand')
    parser.add_argument('--color', help='Vehicle colour')
    parser.add_argument('--year', type=str, help='Year of vehicle production')
    parser.add_argument('--fuel', type=str, help='Fuel type')
    parser.add_argument('--reg_num', type=str)
    args = parser.parse_args()
    args_dict = vars(parser.parse_args())
    print(args_dict)
    fin_result = open_file()
    if args.reg_num == 'get':
        flag_regnum = True
        fieldnames = ['D_REG', 'BRAND', 'MODEL', 'MAKE_YEAR', 'COLOR', 'FUEL', 'N_REG_NEW']
    else:
        flag_regnum = False
        fieldnames = ['D_REG', 'BRAND', 'MODEL', 'MAKE_YEAR', 'COLOR', 'FUEL']

    save_to_file(fin_result, fieldnames)
