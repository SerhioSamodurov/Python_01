# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

user_input = None
user_list = []
print('--Сейчас займёмся наполнением списка------')
print('--Вы всегда можете ввести "q" для выхода--')


while True:
    user_input = input('\t* Введите значение: ')    
    if user_input == 'q':
        break
    user_list.append(user_input)

print(f'Первоначальный вид: {user_list}')

# print(user_list)
for i in range(0, len(user_list)-1, 2):
    user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]

print(f'Вид после обработки: {user_list}')   
    
        
    




