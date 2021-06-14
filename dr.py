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
        self.prlist = Prodlist().prodlist
        self.name = 'None'
        self.prtype = 'Not coffee or tea'
        self.price = '0'


class BaseProduct(Product):
    def __init__(self, name):
        super().__init__()
        for product in self.prlist:
            if product['Наименование'] == name:
                self.name = product['Наименование']
                self.prtype = product['Тип']
                self.price = product['Цена']
                break

    def __str__(self):
        return self.prtype + ': ' + self.name + ', Цена: ' + self.price + ' грн'


class Espresso(BaseProduct):
    def __init__(self):
        name = 'Эспрессо'
        super().__init__(name)


class Doppio(BaseProduct):
    def __init__(self):
        name = 'Доппио'
        super().__init__(name)


class Americano(BaseProduct):
    def __init__(self):
        name = 'Американо'
        super().__init__(name)


class Latte(BaseProduct):
    def __init__(self):
        name = 'Латте'
        super().__init__(name)


class BlackTea(BaseProduct):
    def __init__(self):
        name = 'Черный Чай'
        super().__init__(name)


class EarlGrey(BaseProduct):
    def __init__(self):
        name = 'Earl Grey'
        super().__init__(name)


class Bread(BaseProduct):
    def __init__(self):
        name = 'Хлеб'
        super().__init__(name)


class GingerTea(BaseProduct):
    def __init__(self):
        name = 'Имбирный чай'
        super().__init__(name)


class GreenTea(BaseProduct):
    def __init__(self):
        name = 'Зеленый чай'
        super().__init__(name)


class JasminTea(BaseProduct):
    def __init__(self):
        name = 'Зеленый чай с жасмином'
        super().__init__(name)


class Store:
    def __init__(self, amount=5):
        self.pricelist = [Espresso, Doppio, Americano, Latte, BlackTea, EarlGrey, Bread,
                          GingerTea, GreenTea, JasminTea]

        self.available = [prod() for i in range(amount) for prod in self.pricelist]
        self.balance = 0
        self.earn = []

    @property
    def coffee(self):
        coffee_list = [prod.name for prod in self.available if prod.prtype == 'coffee']
        coffee_dict = dict((x, coffee_list.count(x)) for x in set(coffee_list))
        return coffee_dict

    @property
    def tea(self):
        tea_list = [prod.name for prod in self.available if prod.prtype == 'tea']
        tea_dict = dict((x, tea_list.count(x)) for x in set(tea_list))
        return tea_dict

    @property
    def allgoods(self):
        allgoods_list = [prod.name for prod in self.available]
        allgoods_dict = dict((x, allgoods_list.count(x)) for x in set(allgoods_list))
        return allgoods_dict

    @property
    def values(self):
        values = [int(prod.price) for prod in self.available]
        return sum(values)

    def sell(self, product: str, qnt=1):
        index = 0
        for prod in self.available:
            if product == prod.name:
                self.available.remove(prod)
                self.balance += int(prod.price)
                self.earn.append(prod)
                index += 1
            if index == qnt:
                break


pumpkin = Store()
print(pumpkin.pricelist)
print(pumpkin.coffee)
print(pumpkin.tea)
print(pumpkin.allgoods)
print(pumpkin.values)
pumpkin.sell('Эспрессо')
print(pumpkin.allgoods)
print(pumpkin.values)
print(pumpkin.balance)
print(pumpkin.earn)
print(Bread)
