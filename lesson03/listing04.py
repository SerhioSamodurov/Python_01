def my_func(x, y=-2):
    """ Функция возвращает число возведённое в степень """
    result = x ** y
    return result


# result = my_func(2)
# print(result)


def my_func_2(x, y=-2):
    """ Функция возвращает число возведённое в степень """
    y = abs(y)
    count = 1
    for i in range(y):
        count *= x
    if y >= 0:
        return count
    else:
        return 1 / count


# result = my_func_2(2)
# print(result)
