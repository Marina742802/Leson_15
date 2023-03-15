#Калькулятор. Создать класс, где реализованы методы математических операция (+-/*)
# и функция (вне класса) для ввода данных.
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def divide(self, a, b):
        return a / b
    def multiply(self, a, b):
        return a * b
odj = Calculator()
while True:
   a = int(input('Введите первое число: '))
   b = int(input('Введите первое число: '))
   sign = input('Введите операцию (+-/*): ')
   if sign == '+':
       print(a, '+' , b,'=', odj.add(a, b))
   elif sign == '-':
       print(a, '-', b, '=', odj.subtract(a, b))
   elif sign == '*':
       print(a, '*', b, '=', odj.multiply(a, b))
   elif sign == '/':
      if b != 0:
          print(a, '/', b, '=', odj.divide(a, b))
      else:
          print('На ноль делить нельзя!')

