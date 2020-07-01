# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа
# данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не
# запрашивать у пользователя, а указать явно, в программе.

# We need to create a list
list_of_types = []

# We need to create elements for this list

type_int = 1
type_str = 'it is a string'
type_list = ['1', 2, '3', 4]
type_tuple = (1, '2', 3)
type_set = {1, 2, 3}
type_dict = {1: '2', 3: '4'}
type_bool = True

# Adding the elements to the list

list_of_types.append(type_int)
list_of_types.append(type_str)
list_of_types.append(type_list)
list_of_types.append(type_tuple)
list_of_types.append(type_set)
list_of_types.append(type_dict)
list_of_types.append(type_bool)

# Let's check the types of created elements

for element in list_of_types:
    print(type(element))


