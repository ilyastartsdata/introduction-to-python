# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и введите в формате
# чч:мм:сс. Использовайте форматирование строк

def converter(sec):
    sec = sec % (24 * 3600)
    h = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60

    return "%02d:%02d:%02d" % (h, min, sec)


seconds_provided = int(input('Please provide the seconds you want to convert: '))
print(converter(seconds_provided))

