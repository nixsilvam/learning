import requests
import argparse
import datetime as dt
import json
import os
from pprint import pprint


def value_check():
    cur_folder = os.path.dirname(os.path.abspath(__file__))
    symbols_file = os.path.join(cur_folder, 'symbols.json')
    _from_ = args.currency_from
    _to_ = args.currency_to
    with open(symbols_file, 'r+', encoding='UTF-8') as f:
        symbs = json.load(f)['symbols']
        for n in symbs:
            if _from_ != n:
                _from_ = 'USD'
            if _to_ != n:
                _to_ = 'UAH'
    _amount_ = args.amount
    if args.start_date:
        _start_date = dt.datetime.strptime(args.start_date, '%Y-%m-%d')
        if _start_date > dt.datetime.strptime(t, '%Y-%m-%d'):
            _start_date = t
    else:
        _start_date = t
    return _from_, _to_, _amount_, _start_date


def main(cur_f, cur_t, am, st_da):
    url = 'https://api.exchangerate.host/convert?'
    title = ['date', 'from', 'to', 'amount', 'rate', 'result']
    result_list = []
    while st_da <= dt.datetime.strptime(t, '%Y-%m-%d'):
        response = requests.get(url, params={'from': cur_f, 'to': cur_t, 'amount': am, 'date': st_da}).json()
        results = [response['date'], response['query']['from'], response['query']['to'], response['query']['amount'],
                   response['info']['rate'], response['result']]
        result_list.append(results)
        st_da += dt.timedelta(days=1)
    final_list = [title, *result_list]
    return final_list


if __name__ == '__main__':
    t = dt.datetime.now().strftime('%Y-%m-%d')
    parser = argparse.ArgumentParser(description='description...')
    parser.add_argument('currency_from', type=str)
    parser.add_argument('currency_to', type=str)
    parser.add_argument('amount', type=float, default=100.00, nargs='?')
    parser.add_argument('--start_date', type=str, default=t)
    args = parser.parse_args()
    currency_from, currency_to, amount, start_date = value_check()
    pprint(main(currency_from, currency_to, amount, start_date))
