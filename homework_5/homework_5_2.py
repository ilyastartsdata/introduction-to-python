# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк,
# количества слов в каждой строке.

my_file = open('test2.txt', 'r')
content_of_file = my_file.read()
print(f'The content of the file is: \n {content_of_file}')

my_file = open('test2.txt', 'r')
content_of_file = my_file.readlines()
print(f'The number of lines in the file is {len(content_of_file)}')

my_file = open('test2.txt', 'r')
content_of_file = my_file.readlines()
for i in range(len(content_of_file)):
    print(f'The number of symbols on the {i + 1} line is {len(content_of_file[i])}')

my_file = open('test2.txt', 'r')
content_of_file = my_file.read()
content_of_file = content_of_file.split()
print(f'The number of words is {len(content_of_file)}')
my_file.close()
