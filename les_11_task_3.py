def str_change(input_str: str):
    return max((x for x in input_str.split()), key=len)


print(str_change('What makes a good man'))
