# Пользователь вводит месяц в виде целового числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Solution using the list

month_number = int(input('Please provide the month number: '))
list_of_seasons = ['winter', 'spring', 'summer', 'autumn']
list_winter = [12, 1, 2]
list_spring = [3, 4, 5]
list_summer = [6, 7, 8]
list_autumn = [9, 10, 11]

if type(month_number) == int and month_number in range(1,13):
    if month_number in list_winter:
        print('This month is in the winter ')
    elif month_number in list_spring:
        print('This month is in the spring')
    elif month_number in list_summer:
        print('This month is in the summer')
    else:
        print('This month is in the autumn')
else:
    print('Something is wrong, please try again')

# Solution using the dictionary

dict_of_seasons = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer', 8: "summer", 9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}

month_number = int(input('Please provide the month number: '))

for key, value in dict_of_seasons.items():
    if key == month_number:
        print(value)