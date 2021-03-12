"""Создать вручную список, содержащий цены на товары (10–20 товаров)
A.	Вывести на экран эти цены через запятую в одну строку,
цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
Подумать, как из цены получить рубли и копейки, как добавить нули
B.	Вывести цены, отсортированные по возрастанию, новый список не создавать
(доказать, что объект списка после сортировки остался тот же).
C.	Создать новый список, содержащий те же цены, но отсортированные по убыванию.
D.	Вывести цены пяти самых дорогих товаров.
Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

"""

price_list = [10.02, 15, 100.11, 18, 202.2, 35, 25.24, 240.01, 29.90, 91, 82.3, 48.48484]


# A.
print('задание A')
str_out = ''
for el in price_list:
    cent = int(round(el, 2) * 100 % 100)
    rub = int(el - cent / 100)
    if len(str(cent)) < 2:
        cent = "0" + str(cent)
    str_out = str_out + f"{rub} руб {cent} коп, "
print(str_out[:-2])


# B.
print("задание В")
id_before_sort = id(price_list)
for el_min in price_list:
    for el in price_list[price_list.index(el_min):]:
        if el_min > el:
            el_min, el = el, el_min
            index_el_min = price_list.index(el_min)
            index_el = price_list.index(el)
            price_list.pop(index_el_min)
            price_list.insert(index_el_min, el)
            price_list.pop(index_el)
            price_list.insert(index_el, el_min)
id_after_sort = id(price_list)

str_out = ''
for el in price_list:
    cent = int(round(el, 2) * 100 % 100)
    rub = int(el - cent / 100)
    if len(str(cent)) < 2:
        cent = "0" + str(cent)
    str_out = str_out + f"{rub} руб {cent} коп, "
print(str_out[:-2])

print("объект списка после сортировки остался тот же:", id_before_sort == id_after_sort)
# так как id списка до сортировки и после равны, то объект списка остался тот же


# C.
print("задание C")
price_list_decrement = []
while len(price_list) - len(price_list_decrement) > 1:
    el_max = price_list[0]
    index_max = 0
    for el in price_list[:len(price_list) - len(price_list_decrement)]:
        if el_max < el:
            el_max = el
            index_max = price_list.index(el)
    price_list_decrement.append(el_max)
    price_list.append(el_max)
    price_list.pop(index_max)
price_list_decrement.append(price_list[0])

str_out = ''
for el in price_list_decrement:
    cent = int(round(el, 2) * 100 % 100)
    rub = int(el - cent / 100)
    if len(str(cent)) < 2:
        cent = "0" + str(cent)
    str_out = str_out + f"{rub} руб {cent} коп, "
print(str_out[:-2])


# D.
print("задание D")
for i in range(5):
    el_max = price_list[0]
    for el in price_list:
        try:
            if el > el_max:
                el_max = el
                price_list[price_list.index(el_max)] = str(price_list[price_list.index(el_max)])
        except:
            pass
    cent = int(round(el_max, 2) * 100 % 100)
    rub = int(el_max - cent / 100)
    if len(str(cent)) < 2:
        cent = "0" + str(cent)
    print(f"{rub} руб {cent} коп")