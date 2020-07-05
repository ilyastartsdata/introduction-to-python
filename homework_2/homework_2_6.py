# Реализовать структуру данных "Товары". Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента -
# номер товара и словарь с параметрами (характеристиками товара: название, цена, количество,
# единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# Пример готовой структуры:
#
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
#
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
#
# Пример:
#
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

listings = []
dict_features = {'name': '', 'price': '', 'quantity': '', 'unit': ''}
dict_analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
iterator = 0
feature_ = None
control = None
while True:
    control = input('For quit press [q], for continue press [Enter], for analytics press [a]').upper()
    if control == 'Q':
        break
    iterator += 1
    if control == 'A':
        print(f'\n Current analytics \n {"-" * 30}')
        for key, value in dict_analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in dict_features.keys():
        feature_ = input(f'Please provide the [{f}]: ')
        dict_features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
        dict_analytics[f].append(dict_features[f])
    listings.append((iterator, dict_features))