"""Реализовать проект «Операции с комплексными числами».
Создать класс «Комплексное число». Реализовать перегрузку методов сложения
и умножения комплексных чисел. Проверить работу проекта. Для этого создать
экземпляры класса (комплексные числа), выполнить сложение и умножение созданных экземпляров.
Проверить корректность полученного результата.
"""


class Complexes:
    def __init__(self, cx):
        if not isinstance(cx, str):
            ArithmeticError("Нужен строковый аргумент")
        self.cx = cx

    def __str__(self):
        list_complex = Complexes(self.cx).transformation()
        if list_complex[1] == 1:
            if list_complex[0]:
                return f"({list_complex[0]};i)"
            else:
                return f"i"
        elif list_complex[1] == -1:
            if list_complex[0]:
                return f"({list_complex[0]};-i)"
            else:
                return f"-i"
        elif list_complex[1] == 0:
            return f"{list_complex[0]}"
        else:
            return f"({list_complex[0]};{list_complex[1]}i)"

    def transformation(self):
        """преобразование строки к.ч. (a;bi) к списку
        :return: списoк [a, b] с float элементами
        """
        def correct_imagine(ni):
            """обработка мнимой части
            :param ni: мнимая часть к.ч. (bi)
            :return: 1, -1, float(b) без i
        """
            try:
                ni = float(ni[:-1])
            except ValueError:
                if ni[:-1] == '-':
                    ni = -1
                else:
                    ni = 1
            return ni

        str_complex = self.cx
        str_complex = str_complex.replace(' ', '')
        if str_complex.startswith('('):
            str_complex = str_complex[1:-1]
        if ';' in str_complex:
            str_complex = str_complex.split(';')
            transform_cx = [float(str_complex[0]), float(correct_imagine(str_complex[1]))]
        else:
            if 'i' in str_complex:
                transform_cx = [0, float(correct_imagine(str_complex))]
            else:
                transform_cx = [float(str_complex), 0]
        return transform_cx

    def __add__(self, other):
        if not isinstance(other, Complexes):
            raise ArithmeticError("Второй операнд не комплексное число")
        self.cx = Complexes(self.cx).transformation()
        other.cx = Complexes(other.cx).transformation()
        return Complexes(f"({self.cx[0] + other.cx[0]};"
                         f"{self.cx[1] + other.cx[1]}i)")
        # return [self.cx[0] + other.cx[0], self.cx[1] + other.cx[1]]

    def __mul__(self, other):
        if not isinstance(other, Complexes):
            raise ArithmeticError("Второй операнд не комплексное число")
        self.cx = Complexes(self.cx).transformation()
        other.cx = Complexes(other.cx).transformation()
        return Complexes(f"({self.cx[0] * other.cx[0] - self.cx[1] * other.cx[1]};"
                         f"{self.cx[0] * other.cx[1] + self.cx[1] * other.cx[1]}i)")
        # return [self.cx[0] * other.cx[0] - self.cx[1] * other.cx[1],
        #         self.cx[0] * other.cx[1] + self.cx[1] * other.cx[1]]


for cxn1 in ['(1;1i)', 'i', '(1;1i)', '-5i', '3', '-i']:
    for cxn2 in ['(1;1i)', 'i', '(1;1i)', '-5i', '3', '-i']:
        print(f"{Complexes(cxn1)} + {Complexes(cxn2)} = {Complexes(cxn1) + Complexes(cxn2)}")
        print(f"{Complexes(cxn1)} * {Complexes(cxn2)} = {Complexes(cxn1) * Complexes(cxn2)}")
