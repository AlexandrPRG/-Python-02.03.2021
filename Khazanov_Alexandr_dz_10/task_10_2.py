"""Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое
название.  К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Выполнить общий подсчёт расхода ткани.  Реализовать абстрактные классы
для основных классов проекта и проверить работу декоратора @property.
"""


class Cloth:
    def __init__(self, v: int=0, h: int=0):
        self.V = v  # размер пальто
        self.H = h  # рост костюма

    def outlay_coat(self):
        return self.V / 6.5 + 0.5

    def outlay_suit(self):
        return 2 * self.H + 0.3

    @property
    def outlay(self):
        return ("Общий расход ткани для костюма и пальто " +
                str(round(Cloth.outlay_coat(self) + Cloth.outlay_suit(self), 2)) + " кв.м.")


for size in range(42, 60, 2):
    for growth in range(152, 200, 5):
        print(Cloth(size, growth).outlay)
