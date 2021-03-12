'''Решить задачу 2 не создавая новый список (как говорят, in place)'''

given_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for_finish = len(given_list)
index_insert = 0
for i in range(for_finish + index_insert):
    try:
        int_el = int(given_list[i + index_insert])
        if type(given_list[i + index_insert]) != float:
            str_el = str(given_list[i + index_insert])
            if int_el // 10 == 0:
                if len(str_el) > 1:
                    el = str_el[0] + "0" + str(int_el)
                else:
                    el = "0" + str(int_el)
            else:
                el = str_el
            given_list.insert(i + index_insert, "\"")
            given_list.insert(i + 1 + index_insert, el)
            given_list.insert(i + 2 + index_insert, "\"")
            given_list.pop(i + 3 + index_insert)
        index_insert += 2
    except ValueError:
        pass

print(" ".join(given_list))
