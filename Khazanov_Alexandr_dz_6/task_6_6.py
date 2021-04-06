'''6. Реализовать простую систему хранения данных о суммах продаж булочной.
Должно быть два скрипта с интерфейсом командной строки: для записи данных и
для вывода на экран записанных данных. При записи передавать
из командной строки значение суммы продаж. Для чтения данных реализовать в командной строке
следующую логику:
просто запуск скрипта — выводить все записи;
запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
запуск скрипта с двумя числами — выводить записи, начиная с номера,
равного первому числу, по номер, равный второму числу, включительно.
'''

import sys
name_method = sys.argv[1]
param_methods = sys.argv[2:]
def add_sale(value):
    import sys
    with open("bakery.csv", 'a', encoding='utf-8') as f:
        f.write(str(sys.argv[1]) + "\n")


def show_sales(start_value=0, finish_value=0):
    import sys
    with open("bakery.csv") as f:
        if start_value:
            if finish_value:
                for i in range(1, finish_value + 1):   # 2 args > 0
                    if i < start_value:
                        f.readline()
                    else:
                        print(f.readline())
            else:
                for i, value in enumerate(f, start=1):  # start_value > 0, finish_value = 0, 1 args
                    if i >= start_value:
                        print(value)
        else:
            for val in f:                               # start_value = 0, no args
                print(val)


def edit_sales(number_value, new_val):
    import os
    with open("bakery.csv", 'r+', encoding='utf-8') as f:
        temp_file = open("temp_file", 'a', encoding='utf-8')
        for i, value in enumerate(f, start=1):
            if i == number_value:
                temp_file.write(str(new_val) + "\n")
            else:
                temp_file.write(value)
        temp_file.close()
    os.remove('bakery.csv')
    os.rename('temp_file', 'bakery.csv')


# попытка сделать вызов функции из терминала пока неудачная
getattr(sys.modules[__name__], name_method)(param_methods)
# хотел так сделать, чтобы сохранить первоначальное требование к сдаче ПЗ в виде
# файла task_n_m, так как оно не отменено. В итоге сделал модули, как показано
# в примерах в файле task_6_7
