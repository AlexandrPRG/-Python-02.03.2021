"""Начать работу над проектом «Склад оргтехники».
Создать класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведённых типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


class Warehouse:
    pass


class OfficeEquipment:
    price_equip = float     # цена
    model_equip = str       # модель
    count_equip = int       # количество
    size_equip = list       # размер ШВГ


class Printer(OfficeEquipment):
    type_printer = str      # тип принтера
    speed_print = float     # скорость печати


class Scanner(OfficeEquipment):
    type_matrix = str       # тип матрицы
    dot_inch = int          # разрешение, точек на дюйм
    dept = int              # глубина, бит


class Xerox(OfficeEquipment):
    type_xerox = str        # цветной, чернобелый
    size_copy = str         # размер копии А3, А4
