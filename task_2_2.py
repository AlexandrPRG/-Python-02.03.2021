'''Дан список.
Oбособить каждое целое число (вещественные не трогаем) кавычками
(добавить кавычку до и кавычку после элемента списка, являющегося числом)
и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов

'''

given_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
out_list = []
index_insert = 0
for i, el in enumerate(given_list):
    try:
        int_el = int(el)
        if type(el) != float:
            str_el = str(el)
            if int_el // 10 == 0:
                if len(str_el) > 1:
                    el = str_el[0] + "0" + str(int_el)
                else:
                    el = "0" + str(int_el)
            out_list.insert(i + index_insert, "\"")
            out_list.insert(i + 1 + index_insert, el)
            out_list.insert(i + 2 + index_insert, "\"")
        index_insert += 3
    except ValueError:
        out_list.insert(i + index_insert, el)

print(" ".join(out_list))

