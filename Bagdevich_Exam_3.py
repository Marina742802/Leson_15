#1.	Создайте класс "Студент", который имеет атрибуты имя и возраст,
# а также методы "изменить_имя" и "изменить_возраст".
# Напишите функцию, которая создает объект класса "Студент",
# запрашивая у пользователя его имя и возраст,
# а затем предлагает пользователю изменить имя и возраст.
class Student:
    def __init__(self, name='Marina Bagdevich', age = 49):
        self.name = name
        self.age = age
    def change_name(self):
        return self.name
    def change_age(self):
        return self.age
Vitalik = Student("Vitalik Bagdevich", 25)
print(f'Имя студента - {Vitalik.change_name()}, '
      f'возраст студента - {Vitalik.change_age()}')

#2.	Напишите функцию, которая принимает на вход список чисел
# и возвращает сумму квадратов всех четных чисел в списке.
def summation(x):
    s = 0
    for i in range(1, x+1):
      if i % 2 == 0:
        s += i ** 2
    return s

#3.	Создайте класс "Калькулятор", который имеет атрибуты "значение"
# и методы "сложить", "вычесть", "умножить" и "разделить".
# Напишите функцию, которая создает объект класса "Калькулятор"
# и позволяет пользователю выполнить несколько арифметических операций с его помощью.
class Calculator:
     def __init__(self):
       self.a = float(input('Введите первое число'))
       self.b = float(input('Введите второе число'))
     def add(self): return self.a + self.b
     def mul(self): return self.a * self.b
     def differ(self): return self.a - self.b
     def div(self): return self.a / self.b
while True:
     sign = input('Введите операцию: ')
     if sign not in '+-/*' or sign=='': break
     my_object = Calculator()
     if sign == '+': print(my_object.add())
     elif sign == '-': print(my_object.differ())
     elif sign == '*': print(my_object.mul())
     elif sign == '/': print(my_object.div())
     else:
         print('Такой операции нет')
         break

#4.	Создайте класс "Автомобиль", который имеет атрибуты "марка",
# "модель", "год_выпуска", "цвет" и метод "описание",
# который выводит описание автомобиля в виде строки.
# Напишите функцию, которая создает объект класса "Автомобиль",
# запрашивая у пользователя информацию о марке, модели, годе выпуска и цвете,
# а затем выводит описание автомобиля.
class Car:
    make = 'BMW'
    model = '3-rd'
    year = 1995
    color = 'red'
    def description(self):
      print(f'make - {self.make}, model - {self.model}, '
            f'year - {self.year}, color - {self.color}')
auto = Car()
auto.description()

class Car:
   def __init__(self, a, b, c, x):
       self.make = a
       self.model = b
       self.year = c
       self.color = x
auto = Car('BMW', '3rd', 1995,'red')
print(auto.year, auto.model, auto.color, auto.make)