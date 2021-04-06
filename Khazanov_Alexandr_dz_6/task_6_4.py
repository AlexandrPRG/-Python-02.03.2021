'''4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах
 превышает объём ОЗУ. Также реализовать парсинг данных из файлов -
  получить отдельно фамилию, имя и отчество для пользователей и название каждого хобби:
   преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь).
    Обосновать выбор типа. В словаре должны храниться данные, полученные в результате парсинга.
'''
import sys
user = open('users.csv', encoding='utf-8')
hobby = open('hobby.csv', encoding='utf-8')
list_hobby_user = {}
for line in user:
    el_hobby = hobby.readline()
    if el_hobby:
        list_hobby_user.setdefault(tuple(line[:-1].split(",")),
                               tuple(el_hobby[:-1].split(",")))     # кортеж более удобен для данных
    else:
        list_hobby_user.setdefault(tuple(line[:-1].split(",")))
if hobby.readline():
    sys.exit(1)
else:
    # print(list_hobby_user)
    with open('dict_hobby.csv', 'w', encoding='utf-8') as f:
        f.write(str(list_hobby_user))
user.close()
hobby.close()