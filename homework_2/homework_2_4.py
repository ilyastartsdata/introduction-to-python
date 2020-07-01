# Пользователь вводит строку из нескольких слов, разделенных пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если слово длинное, выводить только
# первые 10 букв в слове.

user_input = input('Please provide values separated by [Space]: ')

user_list = user_input.split()
iterator = 1

for i in user_list:
    if len(i) < 11:
        print(iterator, i)
        iterator += 1
    else:
        print(iterator, i[0:10])
