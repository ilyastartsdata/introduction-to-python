# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль - выручка больше издержек, или
# убыток - издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала
# с прибылью, вычислите рентабельность прибыли к выручке. Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчете на одного сотрудника.

revenue = int(input('Please provide the revenue: '))
costs = int(input('Please provide the costs: '))

result = revenue - costs

if result > 0:
    next_step = 'profit'
    print('Profit')
elif result < 0:
    next_step = 'loss'
    print('Loss')
else:
    next_step = 'zero'
    print('Zero')

if next_step == 'profit':
    number_of_employees = int(input('Please provide the number of employees: '))
    return_on_revenue = result / number_of_employees
    print(return_on_revenue)
else:
    print('Come back once you make the profit')
