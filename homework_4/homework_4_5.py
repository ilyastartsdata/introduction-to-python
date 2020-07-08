# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

def from_100_to_1000_func(i, j):
    return i * j

print(f'List of even items: {[j for j in range(100,1001) if j % 2 == 0]}')
print(f'Result of multiplication of all list items: {reduce(from_100_to_1000_func, [j for j in range(100,1001) if j % 2 == 0])}')