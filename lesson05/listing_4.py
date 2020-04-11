# Создать (не программно) текстовый файл со следующим содержимым:
#
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
dictionary = {}
with open('file_4.txt') as file:
    for line in file.readlines():
        word, integer = line.strip().split(' - ')
        dictionary[word] = integer

dict_2 = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('new.txt', 'w', encoding='utf-8') as file:
    for key, value in dictionary.items():
        if key in dict_2:
            key = dict_2[key]
        print(f'{key} - {value}', file=file)










