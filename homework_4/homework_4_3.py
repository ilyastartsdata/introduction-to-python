# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

print(f'Numbers in the range from 20 to 240, which can be fully divided either by 20 or 21: {[i for i in range(20, 241) if i % 20 ==0 or i % 21 == 0]}')

