"""Продолжить работу над предыдущим заданием.
Реализовать механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад,
нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.
"""


class OfficeEquipment:
    price_equip: float = float      # цена
    model_equip: str = ""           # модель
    count_equip: int = int          # количество
    size_equip: str = ""            # размер ШВГ
    id_equip: int = 0               # регистрационный номер
    list_message = ['Введите цену: ',
                    'Введите модель: ',
                    'Введите количество: ',
                    'Введите размеры через пробел (ШВГ): ']


class ValidationValue:
    def __init__(self, value, value_type):
        self.value = value
        self.value_type = value_type

    def checking(self):
        if self.value_type == float: self.value = self.valid_float()
        elif self.value_type == int: self.value = self.valid_int()
        elif self.value_type == list: self.value = self.valid_list()
        return self.value

    def valid_float(self):
        """ проверка параметра с плавающей точкой
        :return: число float
        """
        while True:
            try:
                float(self.value)
                break
            except ValueError:
                self.value = input("Это должно быть любое число: ")
        return float(self.value)

    def valid_int(self):
        """ проверка ввода целочисленного параметра
        :return: число int
        """
        while True:
            try:
                int(self.value)
                break
            except ValueError:
                self.value = input("Это должно быть целое число: ")
        return int(self.value)

    def valid_list(self):
        """ проверка валидности словаря с размерами оргтехники
        :return: словарь размеров
        """
        while True:
            if len(self.value) != 3:
                self.value = input("Вводите три числа через пробел (Ш В Г): ").split()
            else:
                for el in self.value:
                    el = ValidationValue(el, float).checking()
                return self.value


class Warehouse:
    def __init__(self):
        self.devices = ["Неизвестное устройство", "Принтер", "Сканер", "Ксерокс"]
        self.depts = ['Без отдела',
                      'Отдел устройств вывода',
                      'Отдел устройств ввода',
                      'Отдел устройств копирования']
        self.characteristics = {}

    def receive_equip(self):
        import time
        with open('OfficeEquipment.txt', "a", encoding="utf-8") as f:
            while True:
                print(*self.devices[1:], "(Enter - выйти)")
                device = input('Введите вид техники из списка выше: ').lower()
                if not device:
                    break
                attrs_keys = OfficeEquipment.__annotations__.keys()
                attrs_values = (attr_value for attr_value in
                                OfficeEquipment.__annotations__.values())
                for i, key_attr in enumerate(attrs_keys):
                    if key_attr != 'size_equip':
                        OfficeEquipment.key = ValidationValue(
                            input(OfficeEquipment.list_message[i]),
                            next(attrs_values)).checking()
                    else:
                        break
                OfficeEquipment.id_equip += 1
                OfficeEquipment.size_equip = ValidationValue(
                            input('Введите размеры через пробел (ШВГ): ').split(),
                            list).checking()
                OfficeEquipment.size_equip = {"Ширина": OfficeEquipment.size_equip[0],
                                              "Высота": OfficeEquipment.size_equip[1],
                                              "Глубина": OfficeEquipment.size_equip[2]}

                ind = 0
                for el in self.devices:
                    if el.lower() == device:
                        ind = self.devices.index(el)
                        break
                if ind == 1:
                    self.characteristics = Printer().rec_printer()
                elif ind == 2:
                    self.characteristics = Scanner().rec_scanner()
                elif ind == 3:
                    self.characteristics = Xerox().rec_xerox()
                else:
                    print("Устройство не будет определено")
                    self.characteristics = {}

                f.writelines(
                    f"\n\n{time.asctime()} в {self.depts[ind]} "
                    f"получен {self.devices[ind]} "
                    f"№{OfficeEquipment.id_equip} "
                    f"цена: {OfficeEquipment.price_equip} "
                    f"Количество: {OfficeEquipment.count_equip} "
                    f"Модель: {OfficeEquipment.model_equip} "
                    f"Характеристики: {self.characteristics} "
                    f"Размеры: {OfficeEquipment.size_equip}"
                )


class Printer(OfficeEquipment):
    def __init__(self):
        self.type_printer: str = ""  # тип принтера
        self.speed_print: float = 0  # скорость печати
        self.messages = ["Тип принтера (лазерный итп): ", "Скорость печати: "]

    def rec_printer(self):
        attrs_keys = Printer().__dict__.keys()
        attrs_values = (type(attr_value) for attr_value in
                        Printer().__dict__.values())
        for i, key_attr in enumerate(attrs_keys):
            try:
                Printer().key_attr = ValidationValue(
                    input(Printer().messages[i]),
                    next(attrs_values)).checking()
            except IndexError:
                return {"Тип": self.type_printer, "Скорость печати": self.speed_print}


class Scanner(OfficeEquipment):
    def __init__(self):
        self.type_matrix: str = ''   # тип матрицы
        self.dot_inch: int = 0       # разрешение, точек на дюйм
        self.dept: int = 0           # глубина, бит
        self.messages = ["Тип матрицы (ССD итп): ",
                         "Разрешение матрицы, точек на дюйм: ",
                         "Глубина, бит: "]

    def rec_scanner(self):
        attrs_keys = Scanner().__dict__.keys()
        attrs_values = (type(attr_value) for attr_value in
                        Scanner().__dict__.values())
        for i, key_attr in enumerate(attrs_keys):
            try:
                Scanner().key_attr = ValidationValue(
                    input(Scanner().messages[i]),
                    next(attrs_values)).checking()
            except IndexError:
                return {"Тип матрицы": self.type_matrix,
                        "Разрешение матрицы": self.dot_inch,
                        "Глубина матрицы": self.dept}


class Xerox(OfficeEquipment):
    def __init__(self):
        self.type_xerox: str = ''   # цветной, чернобелый
        self.size_copy: str = ''    # размер копии А3, А4
        self.messages = ["Ксерокс цветной, чернобелый: ",
                         "Размерность копии (А3, А4): "]

    def rec_xerox(self):
        attrs_keys = Xerox().__dict__.keys()
        attrs_values = (type(attr_value) for attr_value in
                        Xerox().__dict__.values())
        for i, key_attr in enumerate(attrs_keys):
            try:
                Xerox().key_attr = ValidationValue(
                    input(Xerox().messages[i]),
                    next(attrs_values)).checking()
            except IndexError:
                return {"Тип": self.type_xerox,
                        "Размерность": self.size_copy}


Warehouse().receive_equip()
