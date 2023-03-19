# В задаче про класс Human дописать 2 класса:
# класс House для создания дома,
# класс Buy_House для его покупки.
# Для того, чтобы в классе Human свойство __house сделать True,
# нужно использовать наследование классов. Но каких? :)
class Human:
    default_name = 'USER'
    default_age = None

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__house = False
        self.__money = 0

    def info(self):
        print(f'Имя: {self.name}, возраст: {self.age}, '
              f'наличие дома: {self.__house}, денег: {self.__money}')

    @staticmethod
    def default_info():
        print(f'Имя по умолчанию: {Human.default_name}, '
              f'возраст по умолчанию: {Human.default_age}')

    def earn_money(self, amount):
        self.__money += amount
        print(f'Получили {amount} рублей. Текущий счет: {self.__money} рублей')


class House(Human):
    def __init__(self, price, area):
        self.price = price
        self.area = area

    def __str__(self):
        return f'Цена: {self.price}, Площадь: {self.area}'


class Buy_House(House):
    def __init__(self, price):
        super().__init__(price, 50)

    def info(self, __house=True):
        return super().__init__(__house)


Human.default_info()
Evgeniy = Human('Евгений', 29)
Evgeniy.info()
Evgeniy.earn_money(100)
Evgeniy.info()
print(Evgeniy._Human__money)

house1 = Buy_House(50000)
house2 = House(150000, 100)
print(house1)
print(house2)
