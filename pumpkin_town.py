from random import randint


class House:

    def __init__(self, _num):
        self.population = randint(1, 101)
        self.num = _num


class Street:

    def __init__(self, _num):
        self.num = _num
        self.houses = []
        self.generate_houses()

    def generate_houses(self):
        for n in range(randint(5, 21)):
            self.houses.append(House(n))
        return self.houses


class PumpkinCity:
    """YOUR FAVORITE TOWN"""
    def __init__(self, cityname):
        self.cityname = cityname
        self.streets = []

    def pump_city(self):
        for n in range(randint(1, 31)):
            self.streets.append(Street(n))

    @property
    def population(self):
        filename = 'population_' + self.cityname
        with open(filename + '.txt', 'w') as f:
            population = 0
            for street in self.streets:
                for house in street.houses:
                    f.write(f'Street #{street.num}\t House #{house.num}\t {house.population}\n')
                    population += house.population
        return f'All population of {self.cityname} is {population}'


if __name__ == '__main__':
    pumpkin = PumpkinCity('Pumpkin')
    pumpkin.pump_city()
    print(pumpkin.population)

    city_17 = PumpkinCity('City-17')
    city_17.pump_city()
    print(city_17.streets)

# пример удаления улиц, с добавлением похожаяя история, а еще это все можно тоже в методы добавить,
# но задча решена итак, исходя из условий :)

    for city17_street in city_17.streets:
        if city17_street.num == 0:
            city_17.streets.remove(city17_street)

    for city17_street in city_17.streets:
        for city17_house in city17_street.houses:
            if city17_house.num == 0:
                city17_street.houses.remove(city17_house)

    print(city_17.population)
