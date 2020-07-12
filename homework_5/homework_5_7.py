# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма
# получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней
# прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

# Importing the necessary packages
import json

# Defining the variables
profit_dict = {}
pr_dict = {}
profit = 0
mean_profit = 0
i = 0

# Starting with the task
with open('test6.txt', 'r') as file_object:
    for line in file_object:
        name, legal_entity, earnings, costs = line.split()
        profit_dict[name] = int(earnings) - int(costs)
        if profit_dict.setdefault(name) >= 0:
            profit = profit + profit_dict.setdefault(name)
            i += 1
    if i != 0:
        mean_profit = profit / i
        print(f'Mean profit is equal to {mean_profit:.2f}')
    else:
        print(f'Mean profit is negative.')
    pr_dict = {'Mean profit': round(mean_profit)}
    profit_dict.update(pr_dict)
    print(f'Profit of each entity {profit_dict}')

with open('test6.txt', 'w') as adjust_js:
    json.dump(profit_dict, adjust_js)

    json_string = json.dumps(profit_dict)
    print(f'The new json file is created with the following contetn: \n '
          f'{json_string}')


