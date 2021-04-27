"""Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверить его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
"""


class DivisionToZero(Exception):
    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    def result_division(self):
        try:
            self.dividend = float(self.dividend)
            self.divider = float(self.divider)
        except ValueError:
            return "Не численный тип аргумента"
        if self.divider == 0: return "Деление невозможно"
        return "Результат: " + str(round(self.dividend / self.divider, 5))


dividend_inp = input("Делимое: ")
divider_inp = input("Делитель: ")
print(DivisionToZero(dividend_inp, divider_inp).result_division())
