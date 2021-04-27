"""Продолжить работу над предыдущим заданием. Разработать методы,
которые отвечают за приём оргтехники на склад и передачу в определённое подразделение
компании.  Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).
"""


class OfficeEquipment:
    price_equip: float = 0     # цена
    model_equip: str = ""      # модель
    count_equip: int = 0       # количество
    size_equip: str = ""       # размер ШВГ
    id_equip: int = 0          # регистрационный номер
    list_message = ['Введите цену: ',
                    'Введите модель: ',
                    'Введите количество: ',
                    'Введите размеры через пробел (ШВГ): ']


class Warehouse:
    def __init__(self):
        self.devices = ["Неизвестное устройство", "Принтер", "Сканер", "Ксерокс"]
        self.depts = ['Без отдела',
                      'Отдел устройств вывода',
                      'Отдел устройств ввода',
                      'Отдел устройств копирования']
        self.characteristics = {}

    def recieve_equip(self):
        import time
        with open('OfficeEquipment.txt', "a", encoding="utf-8") as f:
            while True:
                print(*self.devices[1:], "(Enter - выйти)")
                device = input('Введите вид техники из списка выше: ').lower()
                if not device:
                    break
                attrs = OfficeEquipment.__annotations__.keys()
                for i, key in enumerate(attrs):
                    if key != 'size_equip':
                        OfficeEquipment.key = input(OfficeEquipment.list_message[i])
                    else:
                        break
                OfficeEquipment.id_equip += 1
                OfficeEquipment.size_equip = input('Введите размеры через пробел (ШВГ): ').split()
                OfficeEquipment.size_equip = {"Ширина": OfficeEquipment.size_equip[0],
                                              "Высота": OfficeEquipment.size_equip[1],
                                              "Глубина": OfficeEquipment.size_equip[2]}

                ind = 0
                for el in self.devices:
                    if el.lower() == device:
                        ind = self.devices.index(el)
                        break
                if ind == 1: self.characteristics = Printer().rec_printer()
                elif ind == 2: self.characteristics = Scanner().rec_scanner()
                elif ind == 3: self.characteristics = Xerox().rec_xerox()
                else:
                    print("Устройство не будет определено")
                    self.characteristics = {}

                f.writelines(
                            f"\n\n{time.asctime()}\nв {self.depts[ind]} "
                            f"получен {self.devices[ind]}\n"
                            f"№ {OfficeEquipment.id_equip}\n"
                            f"цена {OfficeEquipment.price_equip}\n"
                            f"Количество {OfficeEquipment.count_equip}\n"
                            f"Модель {OfficeEquipment.model_equip}\n"
                            f"Характеристики: {self.characteristics}\n"
                            f"Размеры: {OfficeEquipment.size_equip}"
                            )


class Printer(OfficeEquipment):
    def __init__(self):
        self.type_printer: str = ""     # тип принтера
        self.speed_print: float = 0     # скорость печати
        self.messages = ["Тип принтера (лазерный итп): ", "Скорость печати: "]

    def rec_printer(self):
        attrs = self.__annotations__.keys()
        for i, key in enumerate(attrs):
            try:
                self.key = input(self.messages[i])
            except IndexError:
                return {"Тип": self.type_printer, "Скорость печати": self.speed_print}


class Scanner(OfficeEquipment):
    def __init__(self):
        self.type_matrix: str = ''     # тип матрицы
        self.dot_inch: int = 0         # разрешение, точек на дюйм
        self.dept: int = 0             # глубина, бит
        self.messages = ["Тип матрицы (ССD итп): ",
                         "Разрешение матрицы, точек на дюйм: ",
                         "Глубина, бит: "]

    def rec_scanner(self):
        attrs = self.__annotations__.keys()
        for i, key in enumerate(attrs):
            try:
                self.key = input(self.messages[i])
            except IndexError:
                return {"Тип матрицы": self.type_matrix,
                        "Разрешение матрицы": self.dot_inch,
                        "Глубина матрицы": self.dept}


class Xerox(OfficeEquipment):
    def __init__(self):
        self.type_xerox: str = ''       # цветной, чернобелый
        self.size_copy: str = ''        # размер копии А3, А4
        self.messages = ["Ксерокс цветной, чернобелый: ",
                         "Размерность копии (А3, А4): "]

    def rec_xerox(self):
        attrs = self.__annotations__.keys()
        for i, key in enumerate(attrs):
            try:
                self.key = input(self.messages[i])
            except IndexError:
                return {"Тип": self.type_xerox,
                        "Размерность": self.size_copy}


Warehouse().recieve_equip()
