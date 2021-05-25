import re


def number_format(string: str):
    numb_match = re.match(r'(\d{3})(\d{3})(\d{2})(\d{2})', string)
    if numb_match:
        numb_list = numb_match.groups()
        if numb_list[0] == '0':
            n = ''.join(numb_list)
            return '(+38) ' + n[0:3] + ' ' + n[3:6] + '-' + n[6:8] + '-' + n[8:10]
        else:
            return 'Failed to recognize number'
    else:
        return 'Failed to recognize number'


if __name__ == '__main__':
    print(number_format('+3806399-999-99'))
    print(number_format('063-999-99-99'))
    print(number_format('063-99999-99'))
    print(number_format('380639999999'))
    print(number_format('+3806399-999-99358768256'))
    print(number_format('+3806399-999-'))
