# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('file_5.txt', 'w+') as file:
    file.write('1 2 3 4 5 6')
    if file.tell() != 0:
        file.seek(0)

    my_list = sum([int(i) for i in file.readline() if i != ' '])












