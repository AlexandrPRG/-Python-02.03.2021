'''Написать функцию thesaurus_adv(),
принимающую в качестве аргументов строки в формате
«Имя Фамилия» и возвращающую словарь, в котором ключи —
первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания
и содержащие записи, в которых фамилия начинается с соответствующей буквы.
Как поступить, если потребуется сортировка по ключам?

'''


def thesaurus_adv(*full_names):
    '''составление словаря из имен и фамилий
    :param full_names: входящие строки ФИО
    :return: словарь с ключом по первой букве фамилии и вложенный словарь
    с ключом по первой букве имени

    '''
    dict_out = {}
    for fn in full_names:
        key_last_name, key_first_name = fn.split()[1][0], fn.split()[0][0]
        if key_last_name in dict_out.keys():
            dict_name = dict_out[key_last_name]
            if key_first_name in dict_name.keys():
                # добавить dict_name
                dict_temp = dict_name[key_first_name].append(fn)
            else:
                # создать dict_name
                dict_temp = dict.fromkeys(key_first_name, [fn])
                # добавить dict_out
                dict_out[key_last_name].update(dict_temp)
        else:
            if key_last_name in dict_out.keys():
                # добавить dict_name
                dict_temp = dict_name[key_first_name].append(fn)
                # создать dict_out
                dict_out.setdefault(key_last_name, dict_temp)
            else:
                # создать dict_name
                dict_temp = dict.fromkeys(key_first_name, [fn])
                # создать dict_out
                dict_out.setdefault(key_last_name, dict_temp)
    return dict_out


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
