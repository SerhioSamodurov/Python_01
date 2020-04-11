# Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
from itertools import count, cycle

for i in count(1):
    if i >= 101:
        break
    else:
        print(i)


my_cats = ['Саймон', 'Бонифаций', 'Сэм']
repeat = 0

for cat in cycle(my_cats):
    if repeat > 20:
        break
    else:
        print(cat)

    repeat += 1

