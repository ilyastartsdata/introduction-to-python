# Реализовать структуру "Рейтинг", представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют
# элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

# Hard coded list of values
rating_list = [7, 5, 3, 3, 2]

# Communication with the user
print(f'Rating - {rating_list}')
n = int(input('Please provide the integer: '))

# Solution
for element in range(len(rating_list)):
    if rating_list[element] == n:
        rating_list.insert(element + 1, n)
        break
    elif rating_list[0] < n:
        rating_list.insert(0, n)
    elif rating_list[-1] > n:
        rating_list.append(n)
    elif rating_list[element] > n and rating_list[element + 1] < n:
        rating_list.insert(element + 1, n)

# Communication with the user
print(f'Updated rating - {rating_list}')
