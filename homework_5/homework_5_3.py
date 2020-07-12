# Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов. Определить, кто из сотрудников
# имеет оклад менее 20 тыс., вывести вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('salary_overview.txt', 'r') as my_file:
    salary = []
    below_20 = []
    info_list = my_file.read().split('\n')
    for i in info_list:
        i = i.split()
        if int(i[1]) < 20000:
            below_20.append(i[0])
        salary.append(i[1])
print(f'The salary below 20000 {below_20}, the mean result is {sum(map(int, salary)) / len(salary)}')
