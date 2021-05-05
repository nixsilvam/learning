import csv
import os
import argparse


def chek_args(row):
    dict_args = {k: v for k, v in args_dict.items() if v is not None}
    del dict_args['o']
    save_flag = False
    for k, v in dict_args.items():
        if row[k] == v:
            save_flag = True
        else:
            save_flag = False
    return save_flag


def open_file():
    cur_folder = os.path.dirname(os.path.abspath(__file__))
    vehicles_file = os.path.join(cur_folder, args.o)
    with open(vehicles_file, 'r+', encoding='UTF-8') as f:
        csv_reader = csv.DictReader(f, ('BRAND', 'COLOR', 'MAKE_YEAR', 'FUEL'), delimiter=';')
        with open('csvfile.csv', 'w+', encoding='UTF-8') as f1:
            csv_writer = csv.DictWriter(f1, 'D_REG BRAND MODEL COLOR MAKE_YEAR FUEL NEW_REG_NEW')
            csv_writer.writerows(list(csv_reader))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='description...')
    parser.add_argument('o', type=str, default='tz_opendata_z01012021_po01042021.csv', nargs='?')
    parser.add_argument('--brand', type=str, help='Vehicle brand', default='')
    parser.add_argument('--color', help='Vehicle colour', default='')
    parser.add_argument('--year', type=str, help='Year of vehicle production', default='')
    parser.add_argument('--fuel', type=str, help='Fuel type', default='')
    parser.add_argument('--reg_num', nargs='?')
    args = parser.parse_args()
    if args.brand == '' and args.color == '' and args.year == '' and args.fuel == '':
        import sys
        sys.exit(0)
    else:
        args_dict = vars(parser.parse_args())
    print(args_dict)
    open_file()


