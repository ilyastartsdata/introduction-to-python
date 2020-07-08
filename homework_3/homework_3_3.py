# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
# двух аргументов.

def my_func(a, b, c):
    if a >= c and b >= c:
        return a + b
    elif b < a < c:
        return a + c
    else:
        return b + c


print(
    f'Your result is {my_func(int(input("Enter the first argument: ")), int(input("Enter the second argument: ")), int(input("Enter the third argument: ")))}')
