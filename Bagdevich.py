# 1. Написать рекурсивную функцию, которая определяет, является ли строка палиндромом
# (одинаково читается в обе стороны: герег, лол, мам, level и тд.)

def is_palindrome(stroka):
    if len(stroka) < 2:
        return True
    elif stroka[0] != stroka[-1]:
        return False
    else:
        return is_palindrome(stroka[1:-1])
 #нужно заполнить этот return, чтобы функция стала рекурсивной и работала правильно

#2. Написать рекурсивную функцию для подсчета количества элементов в списке.
def sum_el(y):
    count = 0
    for x in y:
        count += x
    return count
print(sum_el([8, 3, 6, 1]))

#3. Этот код отсортирует список строк по последнему символу в каждой строке.
# Здесь использована лямбда-функция в качестве ключа в сортировке.
# Измените код так, чтобы сортировка была по второму символу каждой строки

strings = ['apple', 'banana', 'cherry', 'date']
sorted_strings = sorted(strings, key=lambda s: s[2])
print(sorted_strings)
# Output: ['cherry', 'date', 'apple', 'banana']

#4. Напишите функцию make_adder(n),
# которая принимает целое число n и возвращает внутреннюю функцию,
# которая может прибавлять этот n к любому другому целому числу.

def make_adder(n):
    def adder(y):
        return n + y
    return adder
print(make_adder(3)(9))

#5. Напишите функцию counter(), которая возвращает внутреннюю функцию increment(),
# которая увеличивает счетчик на 1 каждый раз, когда она вызывается.

def counter(func):
    def increment(func1):
        increment.count += 1
        return func(func1)

    increment.count = 0
    return increment
