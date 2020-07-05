# Реализовать фунцию, принимающую два числа (полезные аргументы) и выполняющую их деление. Числа запрашивать
# у пользователя, предусмотреть обработку деления на ноль.


def division(*arguments):
    try:
        dividend = int(input('Please provide the number you want to divide: '))
        divider = int(input('Please provide the divider: '))
        result = dividend / divider
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return 'Unfortunately, you cannot divide by 0'

    return result

print(f'result  {division()}')

