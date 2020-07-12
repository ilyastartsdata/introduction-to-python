# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.

def summary():
    try:
        with open('test4.txt', 'w+') as i:
            new_line = input('Provide the numbers separated by space \n')
            i.writelines(new_line)
            j = new_line.split()

            print(sum(map(int, j)))
    except IOError:
        print('Something is wrong with the file')
    except ValueError:
        print('Something is wrong with the input-output')


summary()
