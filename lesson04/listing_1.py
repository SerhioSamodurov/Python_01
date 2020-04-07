# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv
from decimal import Decimal
# тут можно было выделить функции в другой модуль, но для удобства проверки не стал этого делать


def calculation(work_hours, rate_hours, bonus=0):
    """ Функция производит расчёт показателя заработной платы """
    salary = Decimal(work_hours) * Decimal(rate_hours) + Decimal(bonus)
    return salary


def help_func():
    """ Функция выводит справку по использованию скрипта при помощи команды help """
    print("""
          Программа принимает на ввод команду help для вывода справки.
          Для подсчёта заработной платы используется 3 аргумента:
          1.выработка в часах;
          2.ставка в час;
          3.премия (не является обязательным).
          
          Прошу обратить внимание на то, что вводить нужно целые или вещественные числа 
          иначе получите ошибку скрипта.   
          
          Также если вы введете больше аргументов или не предусмотренную команду скрипт не сработает.       
         """)

yardage = len(argv[1:])

try:
    if argv[1] == 'help':
        # print('--Здесь могла бы быть ваша функция--')
        help_func()
    elif yardage == 2:
        work_hours, rate_hours = argv[1:]
        salary = calculation(work_hours, rate_hours)
        print(f'Заработная плата без премии: {salary}')
    elif yardage == 3:
        work_hours, rate_hours, bonus = argv[1:]
        salary = calculation(work_hours, rate_hours, bonus)
        print(f'Заработная плата c премией: {salary}')
    elif yardage > 3:
        print('Вы ввели слишком много аргументов')
        print('Вы можете ознакомиться со справкой введя команду "help" в оболочке командной строки.')
except IndexError as error:
    print('Необходимо ввести больше аргументов')
    print('Вы можете ознакомиться со справкой введя команду "help" в оболочке командной строки.')
except ValueError:
    print('Для расчёта зп необходимо ввести числа')
    print('Вы можете ознакомиться со справкой введя команду "help" в оболочке командной строки.')
