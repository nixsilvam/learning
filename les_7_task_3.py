import requests
import time
from datetime import datetime


def weather(city, days):
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily?' \
          'units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8'
    response = requests.get(url, params={'q': city, 'cnt': days}).json()
#   print(response)  -- для себя чтобы удобнее было смотреть :)
    return response


def user_inp():
    city = input('Enter a city: ')
    days = int(input('Enter the quantity of days: '))
    return city, days


def file_write(response, city, days):
    name = time.strftime('%d_%m_%y') + '_' + str(city) + '_' + str(days) + '_' + 'weather_forecast.txt'
    f = open(name, 'w')
    f.write('Date:\t\t Day temperature:\t Feels like:\t Night temperature:\t\t Feels like:\n')
    for n in response['list']:
        f.write(str(datetime.fromtimestamp(n['dt']).strftime('%d-%m-%y')) + '\t ')
        f.write(str(n['temp']['day']) + '\t\t\t\t ')
        f.write(str(n['feels_like']['day']) + '\t\t\t ')
        f.write(str(n['temp']['night']) + '\t\t\t\t\t ')
        f.write(str(n['feels_like']['night']) + '\n')
    f.close()


x, y = user_inp()
# x, y = 'Odesa', 5
weather_response = weather(x, y)
file_write(weather_response, x, y)
