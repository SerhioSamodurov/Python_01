user_second = int(input('Введите время в секундах: '))

# Конвертация
hour = int(user_second / 3600)
minute = (user_second // 60) % 60
second = user_second % 60

if hour < 10:
    hour = '0' + str(hour)
if minute < 10:
    minute = '0' + str(minute)
if second < 10:
    second = '0' + str(second)

print(f'Перевод: {hour}:{minute}:{second}')
