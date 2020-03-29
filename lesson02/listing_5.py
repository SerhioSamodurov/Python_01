# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.


user_input = int(input('Введите число: '))
my_list = [7, 5, 3, 3, 2]

for number in range(len(my_list)):
    if user_input == my_list[number]:
        my_list.insert(number + 1, user_input)
        break
    else:
        if user_input > max(my_list):
            my_list.insert(0, user_input)
            break
        elif user_input < min(my_list):
            my_list.append(user_input)
            break

print(my_list)
    
    
   
        
    

