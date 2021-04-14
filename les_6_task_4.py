import json
import datetime


def sum_duration():
    sum = 0
    with open('acdc.json', 'r+') as file:
        dict_json_acdc = json.load(file)
        s = dict_json_acdc['album']['tracks']['track']
        duration = [track['duration'] for track in s]
        for y in duration:
            sum += int(y)

    print(str(datetime.timedelta(seconds=sum)))


sum_duration()
