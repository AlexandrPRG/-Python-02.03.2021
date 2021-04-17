"""Реализуйте базовый класс Car:
●	у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда);
●	опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
●	добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля;
●	для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
"""


class Car:
    def __init__(self, name, color, is_police: bool, speed):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        if self.is_police:
            self.name = self.name + " полицейская"

    def go(self):
        print("машина", self.name, self.color, "поехала")

    def stop(self):
        print("машина", self.name, self.color, "остановилась")

    def turn(self):
        from random import choice as direction
        print("машина", self.name, self.color, "едет",
              direction(['налево', 'направо', 'прямо']))

    def show_speed(self):
        print("Текущая скорость:", self.speed)


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print("Cкорость превышена на", self.speed - 60, "км/ч")
        else:
            print("Текущая скорость:", self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Cкорость превышена на", self.speed - 40, "км/ч")
        else:
            print("Текущая скорость:", self.speed)


class PoliceCar(Car):
    pass


for what_car in [PoliceCar, WorkCar, SportCar, TownCar]:
    for name_car in ['гольф', 'тойота', 'додж']:
        for clr in ['черная', 'белая', 'синяя']:
            for police in [True, False]:
                for speed in [20, 45, 65, 50, 120]:
                    print(what_car.__name__,
                          what_car(name_car, clr, police, speed).go())
                    print(what_car.__name__,
                          what_car(name_car, clr, police, speed).show_speed())
                    print(what_car.__name__,
                          what_car(name_car, clr, police, speed).turn())
                    print(what_car.__name__,
                          what_car(name_car, clr, police, speed).stop())
