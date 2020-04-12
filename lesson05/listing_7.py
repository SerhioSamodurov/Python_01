import json

x_list = []

with open('file_7.txt', encoding='utf-8') as file:
    x_dict = {}
    for line in file.readlines():
        firm, form, revenue, cost = line.split()
        x_dict[firm] = int(revenue) - int(cost)
    x_list.append(x_dict)

    y_dict = {}
    counts = 0
    profit = 0

    for val in x_dict.values():
        if val > 0:
            profit += val
            counts += 1
    y_dict['average_profit'] = profit/counts

    x_list.append(y_dict)


with open('data.json', 'w') as file:
    json.dump(x_list, file)


