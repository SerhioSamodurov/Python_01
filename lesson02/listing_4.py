# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

user_input = input('Введите строку, соcтоящую из нескольких произвольных слов: ')
my_words = user_input.split()

for number, my_word in enumerate(my_words, start=1):
    my_word = my_word[:10] if len(my_word) > 10 else my_word
    print(f'{number}. {my_word}')
