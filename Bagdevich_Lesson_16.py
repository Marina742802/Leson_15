# 1. Создайте класс Person, который имеет атрибуты name и age,
# а также метод greet() (выводит приветствие на экран с именем персоны).
class Person:
    name = 'Marina Bagdevich'
    age = 49
    def greet(self):
        pass
    print(f'Hi, my name {name}. I am {age} years old')
person = Person()


class Person:
    name = 'Marina Bagdevich'
    age = 49
    def greet(self):
            print(self.name, self.age)
person = Person()
person.greet()

# 2. Создайте класс Car, который имеет атрибуты make, model и year,
# а также метод get_info() (возвращает строку, содержащую информацию о машине).

class Car:
    make = 'miniven'
    model = 'BMW'
    year = 1998
    def get_info(self):
        print(self.model, self.make, self.year)

car = Car()
car.get_info()
