"""Написать функцию currency_rates(), принимающую в качестве аргумента
код валюты (USD, EUR, ...) и возвращающую курс этой валюты по отношению к рублю.
Использовать библиотеку requests. В качестве API можно использовать
http://www.cbr.ru/scripts/XML_daily.asp.
Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float.
Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты,
которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того,
в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро
"""

def currency_rates(tiker):
    """
    :code:   код тикера валюты
    :return: курс валюты
    """

    import requests

    api_str = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if api_str.status_code == 200:
        api_str = str(api_str.content)
        if api_str.find(tiker.upper()) < 0:
            return None
        else:
            api_str = api_str[api_str.find(tiker.upper()):]
            return float(api_str[:api_str.find("/Value>")][-8:-1].replace(",", "."))
    else:
        return "Соединение не установлено, ошибка: " + str(api_str.status_code)


# decimal вариант: требует импорта дополнительного модуля и настройки числа,
# что добавляет две лишние строки кода
def currency_rates_decimal(tiker):
    import requests
    import decimal

    decimal.getcontext().prec = 5
    api_str = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if api_str.status_code == 200:
        api_str = str(api_str.content)
        if api_str.find(tiker.upper()) < 0:
            return None
        else:
            api_str = api_str[api_str.find(tiker.upper()):]
            return decimal.Decimal(api_str[:api_str.find("/Value>")][-8:-1].replace(",", "."))
    else:
        return "Соединение не установлено, ошибка: " + str(api_str.status_code)

print("Курс USD", currency_rates('usd'))
print("Курс EUR", currency_rates('euR'))   # регистронезависимость
print("Курс VALUTA", currency_rates('VALUTA'))