product_list = []
i = 1

while True:
    product_parameters = {'Название': input('Введите наименование товара: '),
                          'Цена': input('Введите цену товара: '),
                          'Количество': input('Введите количество товара: '),
                          'ед.': input('Введите единицу измерения товара(шт./кг.): ')}
    print('Добавление товаров в корзину...')
    my_tuple = (i, product_parameters)
    product_list.append(my_tuple)

    user_input = input('\nХотите продолжить(да/нет)? ')
    if user_input == 'нет':
        break
    print('=' * 20)

    i += 1

summary_dict = {}

for number, dicts in product_list:
    for key, value in dicts.items():
        if key not in summary_dict:
            summary_dict.setdefault(key, [value])
        elif value in summary_dict[key]:
            continue
        else:
            summary_dict[key].append(value)

for print_ok in summary_dict:
    print(print_ok, '=>', summary_dict[print_ok])



