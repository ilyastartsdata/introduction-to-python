# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1 Two — 2 Three — 3 Four — 4
# Необходимо
# написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

translation_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
help_file = []
with open('test3.txt', 'r') as i:
    for j in i:
        j = j.split(' ', 1)
        help_file.append(translation_dict[i[0]] + ' ' + i[1])
    print(help_file)

with open('test3.txt', 'w') as k:
    k.writelines(help_file)
