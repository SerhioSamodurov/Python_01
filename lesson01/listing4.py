user_answer = input('Введите целое положительное число: ')
maximum = 0
i = 0

while i < len(user_answer):
    if maximum > int(user_answer[i]):
        maximum = maximum
    else:
        maximum = int(user_answer[i])
    i += 1

print(f'Самая большая цифра: {maximum}')
    
    

