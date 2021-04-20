# -*- coding: utf-8 -*-

d = u'\N{DEGREE SIGN}'
C = u'\u2103'
F = u'\u2109'
K = u'\u212a'


def calc_t(t, scale):
    if scale == '' or scale == 'C' or scale == 'С' or scale == 'c' or scale == 'с':
        print(C, '= ', str(t) + d)
        print(F, '= ', str(int(t * 1.8 + 32)) + d)
        print(K, '= ', str(int(t + 273.15)) + K)
    if scale == 'F' or scale == 'f':
        print(C, '= ', str(int((t - 32) / 1.8)) + d)
        print(F, '= ', str(t) + d)
        print(K, '= ', str(int((t + 459.67)) / 1.8) + K)
    if scale == 'K' or scale == 'К' or scale == 'k' or scale == 'к':
        print(C, '= ', str(int(t - 273.15)) + d)
        print(F, '= ', str(int(t * 1.8 - 459.67)) + d)
        print(K, '= ', str(t) + K)


def user_inp():
    t = int(input('Enter a temperature t' + d + r': '))
    scale = (input('Select temperature scale (C for ' + C + ' (default), K for Kelvins, F for ' + F + r'): '))
    return t, scale


x, y = user_inp()
calc_t(x, y)
