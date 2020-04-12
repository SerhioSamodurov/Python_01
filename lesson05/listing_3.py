# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('file_3.txt') as file:
    employee = {}
    for line in file.readlines():
        surname, salary = line.split()
        employee[surname] = int(salary)

    salary_list = []
    for surname, salary in employee.items():
        salary_list.append(salary)
        if salary < 20000:
            print(f'Оклад менее 20 т.р. у  сотрудника с фамилией {surname}.')
    avg = sum(salary_list)/len(salary_list)
    print(f'Ср. зарплата по сотрудникам: {avg} руб.')









