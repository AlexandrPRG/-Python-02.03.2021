'''Реализовать вывод информации о промежутке времени в зависимости от его продолжительности
duration в секундах:
до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.'''

duraction = 3600
sec = duraction % 60
mmin = (duraction - duraction // 3600 * 3600) // 60
hour = (duraction - duraction // 86400 * 86400) // 3600
dday = duraction // 86400
print("duration = ", duraction, "\nВывод ветвлением")
if dday != 0:
    print(f"{dday} дн {hour} час {mmin} мин {sec} сек;")
else:
    if hour != 0:
        print(f"{hour} час {mmin} мин {sec} сек;")
    else:
        if mmin != 0:
            print(f"{mmin} мин {sec} сек;")
        else:
            print(f"{sec} сек;")

"""
цикл для проверки значений может быть таким:
for duraction in range(59, 500000, 58):
    #скрипт
"""
# список можно использовать для помещения в него значений


list_time = ["", duraction // 86400,
             (duraction - duraction // 86400 * 86400) // 3600,
             (duraction - duraction // 3600 * 3600) // 60,
             duraction % 60]
list_dimension_time = ["", "дн", "час", "мин", "сек"]
out_str = ""
for i in range(1, 5):
    if list_time[i] != 0:
        out_str = out_str + f"{list_time[i]} {list_dimension_time[i]} "
print("Вывод со списком: ", out_str)