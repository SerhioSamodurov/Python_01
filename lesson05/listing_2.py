# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('file_2.txt') as file:
    letters = 0
    line_count = 0
    for line in file.readlines():
        letters += len(line.strip())
        line_count += 1
    print(f'Количество строк: {line_count}\nКоличество букв: {letters}')






