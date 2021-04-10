"""5.	*(вместо 4) Написать скрипт, который выводит статистику для заданной папки
в виде словаря, в котором ключи те же, а значения — кортежи вида
(<files_quantity>, [<files_extensions_list>]), например:
    {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }
Сохраните результаты в файл <folder_name>_summary.json в той же папке,
где запустили скрипт.
"""
import os
import json
# path_input = input("Введите путь для папки ")
path_input = "C:\\Users\я\Documents\LIBRARY"


def upper_bound(val):
    """
    :param val: число
    :return: верхняя граница для val, кратная 10
    """
    m = 10
    for n in range(1, 5000000, m * 10):
        m *= 10
        if m >= val:
            return m


list_size = [os.stat(os.path.join(path_input, file)).st_size
             for file in os.listdir(path_input)]
list_ext = [os.path.splitext(os.path.join(path_input, file))[1][1:].lower()
            for file in os.listdir(path_input)]
if len(list_ext) == len(list_size):
    list_bound = [upper_bound(el) for el in list_size]
    dict_statistic = {}
    for i, val in enumerate(list_ext):
        el_tuple_first, el_tuple_second = 0, []
        if list_bound[i] in dict_statistic.keys():
            el_tuple_first, el_tuple_second = dict_statistic[list_bound[i]][0], \
                                              dict_statistic[list_bound[i]][1]
            el_tuple_first += 1
            if val not in el_tuple_second:
                el_tuple_second.append(val)
            temp_list = [el_tuple_first, el_tuple_second]
            dict_statistic[list_bound[i]] = tuple(temp_list)
        else:
            el_tuple_first = 1
            el_tuple_second.append(val)
            temp_list = [el_tuple_first, el_tuple_second]
            dict_statistic.setdefault(list_bound[i], tuple(temp_list))
    with open(f"{os.path.basename(path_input)}_summary.json", 'w', encoding='utf-8') as f:
        json.dump(dict_statistic, f)
else:
    print("Ошибка папки")
