"""Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования
в исходном списке
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
"""


# "в лоб"
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique = []
unique_index = []
result = []
src_set = set(src)
for el_set in src_set:
    duplicate = 0
    for el_src in src:
        if el_set == el_src:
            duplicate += 1
    if duplicate == 1:
        unique.append(el_set)
for el_un in unique:
    for el_src in src:
        if el_un == el_src:
            unique_index.append(src.index(el_src))
for i in range(len(unique)):
    min_index = min(unique_index)
    result.append(src[min_index])
    unique_index.pop(unique_index.index(min_index))

print("в лоб:", *result)
#
# "не в лоб"
#
result = []
for el in src:
    if len(list(filter(lambda x: x == el, src))) == 1:
        result.append(el)
print("не в лоб:", *result)
