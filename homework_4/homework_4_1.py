# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

def employee_salary():
    try:
        hours_worked = float(input('Hours worked: '))
        rate_per_hour = int(input('Salary per hour defined: '))
        bonus = int(input('Bonus if applicable: '))
        result = hours_worked * rate_per_hour + bonus
        print(f'The salary of this particular employee is: {result} ')
    except ValueError:
        return print('Something is wrong. Please give us a number..')

employee_salary()