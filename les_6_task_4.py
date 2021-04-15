import json
import datetime


def sum_duration():
    with open('acdc.json', 'r+') as file:
        dict_json_acdc = json.load(file)
        s = dict_json_acdc['album']['tracks']['track']
        duration = [int(track['duration']) for track in s]
    print(sum(duration))
    print(str(datetime.timedelta(seconds=sum(duration))))


sum_duration()
