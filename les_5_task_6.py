def some_dict(x):
    x1 = {k: v for k, v in x.items() if v is not None}
    return x1


d = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
print(some_dict(d))
