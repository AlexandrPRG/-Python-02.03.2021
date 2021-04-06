'''Есть два файла: в одном хранятся ФИО пользователей сайта,
а в другом — данные об их хобби. Известно, что при хранении данных
используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
ключи — ФИО, значения — данные о хобби.
Сохранить словарь в файл. Проверить сохранённые данные. Если в файле,
хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать,
что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
'''
import sys
import json
code_stop = 1
with open('users.csv', encoding='utf-8') as fu:
    dict_user_hobby = {line.replace(",", " ")[:-2]:None for line in fu}
with open('hobby.csv', encoding='utf-8') as fh:
    hobby_gen = (line.replace(",", " ")[:-2] for line in fh)
    for user in dict_user_hobby.keys():
        try:
            dict_user_hobby[user] = next(hobby_gen)
        except StopIteration:
            code_stop = 0
    if code_stop:
        try:
            next(hobby_gen)
            sys.exit(1)
        except StopIteration:
            with open('dict_hobby.csv', 'w', encoding='utf-8') as f:
                json.dump(dict_user_hobby, f)
    else:
        with open('dict_hobby.csv', 'w', encoding='utf-8') as f:
            json.dump(dict_user_hobby, f)
# проверка данных в файле
with open('dict_hobby.csv', encoding='utf-8') as f:
    print(json.load(f))
