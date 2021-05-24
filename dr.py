import csv


class Prodlist:
    @property
    def prodlist(self):
        with open('inventory.csv', 'r+', encoding='UTF-8') as File:
            csv_reader = csv.DictReader(File, delimiter=',')
            prodlist = []
            for row in csv_reader:
                prodlist.append(row)
        return prodlist


class Product:

    def __init__(self):
        self.prlist = []
        self.prodlist()
        self.name = 'None'
        self.prtype = 'Not coffee or tea'
        self.price = '0'

    def __str__(self):
        return self.prtype + ': ' + self.name + ', Цена: ' + self.price + ' грн'

    def prodlist(self) -> list:
        with open('inventory.csv', 'r+', encoding='UTF-8') as File:
            csv_reader = csv.DictReader(File, delimiter=',')
            for row in csv_reader:
                self.prlist.append(row)
        return self.prlist

# можно ли создавать подклассы какой-то командой по списку а не вручную? Я что-то упустила?
# А то много повторяющихся строк получается...


class Espresso(Product):
    def __init__(self):
        super().__init__()
        self.name = self.prlist[0]['Наименование']
        self.prtype = self.prlist[0]['Тип']
        self.price = self.prlist[0]['Цена']


class Doppio(Product):
    def __init__(self):
        super().__init__()
        self.name = self.prlist[1]['Наименование']
        self.prtype = self.prlist[1]['Тип']
        self.price = self.prlist[1]['Цена']


class Americano(Product):
    def __init__(self):
        super().__init__()
        self.name = self.prlist[2]['Наименование']
        self.prtype = self.prlist[2]['Тип']
        self.price = self.prlist[2]['Цена']


class Latte(Product):
    def __init__(self):
        super().__init__()
        self.name = self.prlist[3]['Наименование']
        self.prtype = self.prlist[3]['Тип']
        self.price = self.prlist[3]['Цена']


class BlackTea(Product):
    def __init__(self):
        super().__init__()
        self.name = self.prlist[4]['Наименование']
        self.prtype = self.prlist[4]['Тип']
        self.price = self.prlist[4]['Цена']


class EarlGrey(Product):     # с бергамотом <3
    def __init__(self):
        super().__init__()
        self.name = self.prlist[5]['Наименование']
        self.prtype = self.prlist[5]['Тип']
        self.price = self.prlist[5]['Цена']


class Bread(Product):
    def __init__(self):
        super().__init__()
        self.name = self.prlist[6]['Наименование']
        self.price = self.prlist[6]['Цена']


class GingerTea(Product):
    def __init__(self):
        super().__init__()
        self.name = self.prlist[7]['Наименование']
        self.prtype = self.prlist[7]['Тип']
        self.price = self.prlist[7]['Цена']


class GreenTea(Product):
    def __init__(self):
        super().__init__()
        self.name = self.prlist[8]['Наименование']
        self.prtype = self.prlist[8]['Тип']
        self.price = self.prlist[8]['Цена']


class JasminTea(Product):
    def __init__(self):
        super().__init__()
        self.name = self.prlist[9]['Наименование']
        self.prtype = self.prlist[9]['Тип']
        self.price = self.prlist[9]['Цена']


class Store:
    def __init__(self, amount=5):
        self.amount = amount
        self.pricelist = [[Espresso()], [Doppio()], [Americano()], [Latte()], [BlackTea()], [EarlGrey()], [Bread()],
                          [GingerTea()], [GreenTea()], [JasminTea()]]
        self.available = [prod * self.amount for prod in self.pricelist]

    def coffee(self):
        for prod in self.available:
            print(prod.__dict__)




pumpkin = Store()
print(pumpkin.pricelist)
print(pumpkin.available)
pumpkin.coffee()



