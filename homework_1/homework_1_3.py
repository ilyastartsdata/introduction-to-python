# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввел число 3. Считаем 3 + 33 + 333 = 369

n = input('Please please provide the n: ')
n_1 = int(n)
n_2 = int(n+n)
n_3 = int(n+n+n)
result = n_1 + n_2 + n_3
print(result)

