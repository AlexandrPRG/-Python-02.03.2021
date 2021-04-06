'''5. ** (вместо 4) Решить задачу 4 и te.
 Проверить работу скрипта для случая, когда все файлы находятся в разных папках.
'''
import sys
path_users = sys.argv[1]
path_hobby = sys.argv[2]
path_target = sys.argv[3]
user = open(path_users, encoding='utf-8')
hobby = open(path_hobby, encoding='utf-8')
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
    with open(path_target, 'w', encoding='utf-8') as f:
        f.write(str(list_hobby_user))
user.close()
hobby.close()


# команда для терминала
# >python task_6_5.py C:\Users\я\Documents\GEEKBRAINS\python\1_Python\PZ\khazanov_alexandr_dz_6\users.csv C:\Users\я\Documents\GEEKBRAINS\python\1_Python\PZ\khazanov_alexandr_dz_6\hobby.csv C:\Users\я\Documents\GEEKBRAINS\python\1_Python\PZ\khazanov_alexandr_dz_6\dict_hobby.csv
# команда для разных папок
# python task_6_5.py C:\Users\я\Documents\GEEKBRAINS\python\1_Python\users.csv C:\Users\я\Documents\GEEKBRAINS\python\1_Python\hobby.csv C:\Users\я\Documents\GEEKBRAINS\python\1_Python\PZ\dict_hobby.csv
