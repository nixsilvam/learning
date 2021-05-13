import csv
import os
import argparse
import sys


def check_args():
    dict_args = {k: v for k, v in args_dict.items() if v is not None}
    if not dict_args:
        sys.exit(0)
    del dict_args['o']
    map_dict = {'brand': 'BRAND',
                'color': 'COLOR',
                'year': 'MAKE_YEAR',
                'fuel': 'FUEL',
                'reg_num': 'N_REG_NEW'}
    for i in dict_args:
        if i in map_dict:
            dict_args[map_dict[i]] = dict_args.pop(i)
    return dict_args


def check_flag(row, fin_dict):
    save_flag = False
    for k, v in fin_dict.items():
        if row[v] == v:
            save_flag = True
        else:
            save_flag = False
    return save_flag


def open_file():
    result = []
    cur_folder = os.path.dirname(os.path.abspath(__file__))
    vehicles_file = os.path.join(cur_folder, args.o)
    with open(vehicles_file, 'r', encoding='UTF-8') as f:
        csv_reader = csv.DictReader(f, ('BRAND', 'COLOR', 'MAKE_YEAR', 'FUEL', 'N_REG_NEW'), delimiter=';')
        for row in csv_reader:
            if check_flag(row, check_args()):
                result.append(row)
    return result


def file_name(fin_dict):
    name_list = [v for v in fin_dict.values]
    vehicle_name = '_'.join(name_list) + '.csv'
    return vehicle_name


def save_to_file(result, vehicle_name):
    with open(vehicle_name, 'w+', encoding='UTF-8') as f1:
        csv_writer = csv.DictWriter(f1, ('D_REG', 'BRAND', 'MODEL', 'COLOR', 'MAKE_YEAR',
                                         'FUEL', 'NEW_REG_NEW'))
        csv_writer.writerows(result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='description...')
    parser.add_argument('o', type=str, default='tz_opendata_z01012021_po01042021.csv', nargs='?')
    parser.add_argument('--brand', type=str, help='Vehicle brand', default='')
    parser.add_argument('--color', help='Vehicle colour', default='')
    parser.add_argument('--year', type=str, help='Year of vehicle production', default='')
    parser.add_argument('--fuel', type=str, help='Fuel type', default='')
    parser.add_argument('--reg_num', nargs='?')
    args = parser.parse_args()
    args_dict = vars(parser.parse_args())
    print(args_dict)
    final_dict = check_args()
    result_list = open_file()
    final_name = file_name(final_dict)
    save_to_file(result_list, final_name)
