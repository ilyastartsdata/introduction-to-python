# Поработайте с переменными, создайте несколько, выведите на экран
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран

a = 2
b = 7
c = a * b
print(f'a is equal to {a}, b is equal to {b}, multiplication is equal to {c}')

# Конвертер валют из рублей в евро и доллары (вторая произвольная часть задания)

euro_ruble = 78.28
dollar_ruble = 69.78
ruble_dollar = 0.014
ruble_euro = 0.013
dollar_euro = 0.89
euro_dollar = 1.12

answer_1 = input('Please provide us the name of the currency(dollar, euro, ruble): ')
if answer_1 == 'dollar':
    answer_2 = int(input('Are you interested in dollar/euro or dollar/ruble? (1 or 2): '))
    if answer_2 == 1:
        sum_dollars = int(input('Please provide the sum in dollars: '))
        result_dollar_euro = sum_dollars * dollar_euro
        print(f'The dollar sum provided is equal to {result_dollar_euro} euros')
    elif answer_2 == 2:
        sum_dollars = int(input('Please provide the sum in dollars: '))
        result_dollar_ruble = sum_dollars * dollar_ruble
        print(f'The dollar sum provided is equal to {result_dollar_ruble} rubles')
    else:
        answer_2 = int(input('Not sure. Please choose between the option 1 or 2: '))
elif answer_1 == 'euro':
    answer_2 = int(input('Are you interested in euro/dollar or euro/ruble? (1 or 2): '))
    if answer_2 == 1:
        sum_euros = int(input('Please provide the sum in euros: '))
        result_euro_dollar = sum_euros * euro_dollar
        print(f'The euro sum provided is equal to {result_euro_dollar} dollars')
    elif answer_2 == 2:
        sum_euros = int(input('Please provide the sum in euros: '))
        result_euro_ruble = sum_euros * euro_ruble
        print(f'The euro sum provided is equal to {result_euro_ruble} rubles')
    else:
        answer_2 = int(input('Not sure. Please choose between the option 1 or 2: '))
elif answer_1 == 'ruble':
    answer_2 = int(input('Are you interested in ruble/dollar or ruble/euro? (1 or 2): '))
    if answer_2 == 1:
        sum_rubles= int(input('Please provide the sum in rubles: '))
        result_ruble_dollar = sum_rubles * ruble_dollar
        print(f'The ruble sum provided is equal to {result_ruble_dollar} dollars')
    elif answer_2 == 2:
        sum_rubles = int(input('Please provide the sum in rubles: '))
        result_ruble_euro = sum_rubles * ruble_euro
        print(f'The ruble sum provided is equal to {result_ruble_euro} dollars')
    else:
        answer_2 = int(input('Not sure. Please choose between the option 1 or 2: '))
else:
    answer_1 = input('Please choose among the following options dollar/euro/ruble: ')