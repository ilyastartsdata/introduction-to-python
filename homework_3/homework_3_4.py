# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

# Solution using the range()
 def my_func(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    if x >= 0 and y >= 0:
        return 'Please provide the negative integer as power'
    else:
        return 1 / result

# print(my_func(float(input('Please provide the positive value: ')), int(input('Please provide the negative integer: '))))

# Solution using **

def my_func(x, y):
    x = float(input('Please provide the positive real number: '))
    y = int(input('Please provide the negative integer: '))
    if x > 0 and y < 0:
        return x ** y
    else:
        return print('Something is wrong, check the provided values and try again')

print(f'Result is {my_func(float(input("Please provide the positive real number: ")), int(input("Please provide the negative integer: ")))}')
