"""Написать декоратор с аргументом-функцией (callback),
позволяющий валидировать входные значения функции и выбрасывать исключение ValueError,
если что-то не так
"""


def val_checker(func):
    def wrapper(*args, **kwargs):
        for el in args:
            calc = func(el)
            if el > 0:
                return calc
            else:
                raise ValueError("wrong val", el)
    return wrapper


@val_checker
def calc_cube(x):
    return x ** 3


print(calc_cube(-2))