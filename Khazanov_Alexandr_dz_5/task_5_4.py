"""Представлен список чисел.
Необходимо вывести те его элементы, значения которых больше предыдущего
"""


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
generator_from_0 = (el for el in src[:-1])
generator_from_1 = (el for el in src[1:])
for i in range(len(src)-1):
    el_append = next(generator_from_1)
    if el_append > next(generator_from_0):
        result.append(el_append)
print(result)
