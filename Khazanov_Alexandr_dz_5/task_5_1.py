"""Написать генератор нечётных чисел от 1 до n (включительно),
используя ключевое слово yield
"""


def odd_nums(n):
    """генератор нечетных чисел от 1 до n включительно
    :param n: верхняя граница последовательности
    :return: значение последовательности
    """
    if n % 2 == 0:
        for el in (i for i in range(n) if i % 2 != 0):
            yield el
    else:
        for el in  (i for i in range(n+2) if i % 2 != 0):
            yield el


var = odd_nums(22)
for i in range(11):
    print(next(var))


