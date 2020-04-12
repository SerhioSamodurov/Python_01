x_dict = {}
with open('file_6.txt', encoding='utf-8') as file:
    for line in file.readlines():
        lessons, *args = line.split()
        arg = sum([int(i) for i in args if i != '—'])
        x_dict[lessons] = arg









