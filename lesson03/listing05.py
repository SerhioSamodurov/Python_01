def my_func():
    summa = 0
    while True:
        user_input = input('Введите числа через пробел[@ для выхода]: ')
        if '@' in user_input :
            my_list = [int(number) for number in user_input[:-1] if number != ' ']
            summa += sum(my_list)
            print(f'Сумма чисел: {summa}')
            break
        else:
            my_list = [int(number) for number in user_input if number != ' ']
            summa += sum(my_list)
            print(f'Сумма чисел: {summa}')
    return summa

x = my_func()
