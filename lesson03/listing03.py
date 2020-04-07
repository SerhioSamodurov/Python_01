def my_func(x=1, y=2, z=3):
    """ Функция возвращает сумму двух наибольших чисел """
    my_list = list((x, y, z))
    my_list.sort(reverse=True)
    return sum(my_list[:2])

# summa = my_func()
# print(summa)


