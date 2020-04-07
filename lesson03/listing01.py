user_answer_1 = int(input('Введите делимое: '))
user_answer_2 = int(input('Введите делитель: '))


def divide_args(arg1=1, arg2=2):
    try:
        return arg1 / arg2
    except ZeroDivisionError as error:
        print(f'Ошибка: {error}')
        return 0


result = divide_args(user_answer_1, user_answer_2)
print(result)

