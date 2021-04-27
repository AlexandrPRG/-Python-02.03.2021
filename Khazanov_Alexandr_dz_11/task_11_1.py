"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год».  В рамках класса реализовать два метода.
Первый — с декоратором @classmethod. Он должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй — с декоратором @staticmethod,
он должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, str_date):
        cls = Date
        if not isinstance(str_date, str):
            raise ValueError("Вводите строковый формат даты")
        cls.str_date = str_date

    @staticmethod
    def validation_date(day, month, year):
        valid = False
        if 0 < month < 13:
            if month == 4 or month == 6 or month == 9 or month == 11:
                if 0 < day < 31: valid = True
            elif month == 2:
                if year % 4 == 0:
                    if 0 < day < 30: valid = True
                else:
                    if 0 < day < 29: valid = True
            else:
                if 0 < day < 32: valid = True

        if valid:
            return f"Дата {day}/{month}/{year} валидна"
        else:
            return f"Дата {day}/{month}/{year} не валидна"

    @classmethod
    def dmy(cls, str_date):
        if str_date.count('-') == 2:
            date_parsed = str_date.split('-')
            return cls.validation_date(int(date_parsed[0]),
                                       int(date_parsed[1]),
                                       int(date_parsed[2]))
        else:
            return f"Неподдерживаемый формат даты {str_date} (вводить dd-mm-yy"


d = '29-2-91'
print(Date(d).dmy(d))
d = '2.12.91'
print(Date(d).dmy(d))
d = '2-12-91'
print(Date(d).dmy(d))
