# Создать программно файо в текстовом формате, записать в него
# построчно данные, вводимые пользователем. Об окончании ввода данных
# свидетельствует пустая строка.

my_file = open('test.txt', 'w')
new_line = input('Please provide the text \n')
while new_line:
    my_file.writelines(new_line)
    new_line = input('Please provide the text \n')
    if not new_line:
        break

my_file.close()
my_file = open('test.txt', 'r')
content_of_file = my_file.readlines()
print(content_of_file)
my_file.close()
