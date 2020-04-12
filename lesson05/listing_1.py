# Создать программно файл в текстовом формате, записать в
# него построчно данные, вводимые пользователем.Об окончании
# ввода данных свидетельствует пустая строка.


with open('file_1.txt', 'w') as file:
    while True:
        user_line = input('Введите строку:')
        if not user_line:
            break
        file.write(user_line + '\n')



