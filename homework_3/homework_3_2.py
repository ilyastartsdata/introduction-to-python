# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные
# аргументы. Реализовать вывод данных о пользователе одной строкой.

def summary(*information):
    name = input('Please provide the name: ')
    surname = input('Please provide the surname: ')
    year = input('Please provide your year of birth: ')
    city = input('Please provide the city you live in: ')
    email = input('Please share your email: ')
    phone = input('And phone number: ')

    return ' '.join([name, surname, year, city, email, phone])

print(f'Summary: {summary()}')