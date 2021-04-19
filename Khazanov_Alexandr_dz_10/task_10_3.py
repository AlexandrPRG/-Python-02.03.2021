"""Осуществить программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс «Клетка».  В его конструкторе инициализировать параметр,
соответствующий количеству ячеек клетки (целое число).  В классе должны быть реализованы
методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
деление (__floordiv____truediv__()).  Эти методы должны применяться только к клеткам и
выполнять увеличение, уменьшение, умножение и округление до целого числа деления клеток
соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки
должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если
разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки —
произведение количества ячеек этих двух клеток.
Деление. Создаётся общая клетка из двух. Число ячеек общей клетки
определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса
и количество ячеек в ряду. Этот метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n
равно переданному аргументу. Если ячеек на формирование ряда не хватает,
то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5.
В этом случае метод make_order() вернёт строку: *****\n*****\n**.
Или количество ячеек клетки — 15, а количество ячеек в ряду равняется 5.
Тогда метод make_order() вернёт строку: *****\n*****\n*****.
"""


class BioCell:
    def __init__(self, cell: int):
        if not isinstance(cell, int):
            raise ValueError("Количество ячеек - целое число")
        self.cell = cell

    def __add__(self, other):
        if not isinstance(other, BioCell):
            raise ArithmeticError("Второй операнд не клетка")
        return BioCell(self.cell + other.cell)

    def __sub__(self, subtrahend):
        if not isinstance(subtrahend, BioCell):
            raise ArithmeticError("Второй операнд не клетка")
        if self.cell < subtrahend.cell:
            return "Ячеек в клетке должно быть положительное число"
        else:
            return BioCell(self.cell - subtrahend.cell)

    def __mul__(self, multiplier):
        if not isinstance(multiplier, BioCell):
            raise ArithmeticError("Второй операнд не клетка")
        return BioCell(self.cell * multiplier.cell)

    def __truediv__(self, divider):
        if not isinstance(divider, BioCell):
            raise ArithmeticError("Второй операнд не клетка")
        if divider.cell == 0:
            raise ZeroDivisionError("Нельзя разделить на клетку с 0 ячеек")
        return BioCell(self.cell // divider.cell)

    def make_order(self, cell_row):
        def asterisk(vsl):
            """
            :param vsl: число * в строке
            :return: возвращает строку из *
            """
            str_asterisk = ''
            for dig in range(vsl):
                str_asterisk = str_asterisk + "*"
            return str_asterisk

        result = ''
        if self.cell <= cell_row:
            result = asterisk(self.cell)
        else:
            for dig in range(self.cell // cell_row):
                result = result + asterisk(cell_row) + "\n"
            result = result + asterisk(self.cell % cell_row)
        return result


cell_1 = BioCell(10)
cell_2 = BioCell(3)
print("Сумма\n", (cell_1 + cell_2).make_order(8))
print("Разность\n", (cell_1 - cell_2).make_order(8))
print("Произведение\n", (cell_1 * cell_2).make_order(8))
print("Деление\n", (cell_1 / cell_2).make_order(8))
