my_revenue = int(input('Укажите вашу выручку (руб.): '))
my_cost = int(input('Укажите ваши затраты (руб.): '))
efficiency = round((my_revenue - my_cost) / my_revenue, 2)


if my_revenue > my_cost:
    print('Прибыль:')
    print(f'\t* Ваша прибыль составила - {my_revenue - my_cost};')
    print(f'\t* Рентабельность выручки - {efficiency}%')
    number_of_employees = int(input('Сколько сотрудников у вас работает? '))
    print(f'\t* Прибыль на одного сотрудника - {round((my_revenue - my_cost) / number_of_employees, 2)}')
elif my_revenue == my_cost:
    print('Ваши затраты равны выручке.')
else:
    print('Убыток.')
    print(f'Ваши убытки составили - {abs(my_cost - my_revenue)}')
