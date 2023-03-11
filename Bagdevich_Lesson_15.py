# №1. Если в функцию передаётся кортеж, то посчитать длину всех его строк.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – кол-во букв.
# Сделать проверку со всеми этими случаями.
# Использовать готовые типы данных, с клавиатуры ничего не вводится
# Например function([1,2,3,'a','bc8?']) -> 4 числа, 3 буквы
# function((1,2,3,'a','bc8?',7,8,9)) -> 5 символов
# function(788) -> 1
# function('788') -> 0 букв
# №2. Привяжите к предыдущей функции декоратор, который будет выводить информацию о том,
# какой тип данных вы отправили: кортеж, список, число, строку или какой-то другой тип данных
def function(fn):
    def wrapper(W):
        print(f'Тип данных: {type(W)}')
        return fn(W)
    return wrapper
@function

def foo(x):
    if isinstance(x, tuple):
        return sum([len(i) for i in x])
    elif isinstance(x, list):
        return len([i for i in x if str(i).isalpha() or str(i).isdigit()])
    elif isinstance(x, int):
        return len([i for i in str(x) if i in '13579'])
    elif isinstance(x, str):
        return len(x)
    else:
        return 'Тип не определен'

print(foo(('asd', 'qwe', 'ASDFGH')))
print(foo([1, 2, 3, 'abc', 'adas', 123]))
print(foo(1234567))
print(foo('asdfghjk'))
print(foo({'cv': 1, 'bgt': 2}))