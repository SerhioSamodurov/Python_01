# Реализовать формирование списка, используя функцию range() и возможности
# генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов
# списка.
# Подсказка: использовать функцию reduce().
from functools import reduce

x_list = [number for number in range(100, 1001) if number % 2 == 0]
y_int = reduce(lambda x, y: x * y, x_list)
# print(y_int)


