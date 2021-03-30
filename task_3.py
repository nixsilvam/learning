v = int(input('''Enter the Vasya's speed (km/h):'''))
t = int(input("Enter the time of Vasya's rally (in hours):"))
if v >= 0:
    print(v * t)
else:
    print(100 + (v * t))
