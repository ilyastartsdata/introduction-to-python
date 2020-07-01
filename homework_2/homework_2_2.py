# Для списка реализовать обмен значений соседних элементов, т.е. значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


# Found in Internet:
# value_list = [int(element) for element in input('Please provide the value: ').split()]
# for element in range(1, len(value_list), 2):
#     value_list[element - 1], value_list[element] = value_list[element], value_list[element - 1]
# print(' '.join([str(element) for element in value_list]))

list_of_values = []

a = input('Please provide the value for a: ')
b = input('Please provide the value for b: ')
c = input('Please provide the value for c: ')
d = input('Please provide the value for d or skip by pressing [Enter]: ')

if d == '':
    list_of_values.append(a)
    list_of_values.append(b)
    list_of_values.append(c)
    print(f'Values provided: {list_of_values}')
    list_of_values[0], list_of_values[1] = list_of_values[1], list_of_values[0]
    print(f'Result: {list_of_values}')
else:
    list_of_values.append(a)
    list_of_values.append(b)
    list_of_values.append(c)
    list_of_values.append(d)
    print(f'Values provided: {list_of_values}')
    list_of_values[0], list_of_values[1] = list_of_values[1], list_of_values[0]
    list_of_values[2], list_of_values[3] = list_of_values[3], list_of_values[2]
    print(f'Result: {list_of_values}')

# P.S very straightforward and wrong

