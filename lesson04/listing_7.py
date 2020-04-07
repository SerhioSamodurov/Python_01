# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fibo_gen().
#     Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
from math import factorial
from itertools import count


# тест
# print(factorial(4))
# print(factorial(5))

def get_factor():
    for x in count(1):
        yield factorial(x)


generator = get_factor()
counter = 0

for el in generator:
    if counter == 15:
        break
    print(el)
    counter += 1

# тест
# def get_factor(x):
#      if x == 0:
#          return 1
#      else:
#         return get_factor(x - 1) * x
#
# print(get_factor(6))
