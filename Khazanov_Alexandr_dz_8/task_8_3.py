"""Написать декоратор для логирования типов позиционных аргументов функции,
Примечание: если аргументов несколько - выводить данные о каждом через запятую;
 можете ли вы вывести тип значения функции? Сможете ли решить задачу
 для именованных аргументов? Сможете ли вы замаскировать работу декоратора?
calc_cube(5: <class 'int'>)
"""

def type_logger(func):
    def wrapper(*args, **kwargs):
        return type({el: type(el) for el in args}), \
               {el: type(el) for el in args}, func(*args)
    return wrapper


@type_logger
def calc_cube(*args, **kwargs):
    return [arg ** 3 for arg in args]


print(calc_cube(5, 3, 3.3))