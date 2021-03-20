"""*Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
которая передаётся в ответе сервера. Дата должна быть в виде объекта date.
Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
"""
def currency_rates(tiker):
    """
    :code:   код тикера валюты
    :return: курс валюты
    """

    import requests
    import datetime

    api_str = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if api_str.status_code == 200:
        api_str = str(api_str.content)
        if api_str.find(tiker.upper()) < 0:
            return None
        else:
            api_valcurs = api_str[api_str.find(tiker.upper()):]
            api_valcurs = float(api_valcurs[:api_valcurs.find("/Value")][-8:-1].replace(",", "."))
            api_date = api_str[api_str.find("ValCurs Date=") + 14:
                               api_str.find("ValCurs Date=") + 24].split('.')
            api_date = datetime.datetime(day=int(api_date[0]),
                                         month=int(api_date[1]),
                                         year=int(api_date[2]))
            # для извлечения даты воспользуемся f-строкой
            return f"{api_date.day}.{api_date.month}.{api_date.year}", api_valcurs
    else:
        return "Соединение не установлено, ошибка: " + str(api_str.status_code)


# print(currency_rates("usd"))
