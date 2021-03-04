'''Реализовать вывод информации о промежутке времени в зависимости от его продолжительности
duration в секундах:
до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
	Примеры:
duration = 53
53 сек
duration = 153
2 мин 33 сек
duration = 4153
1 час 9 мин 13 сек
duration = 400153
4 дн 15 час 9 мин 13 сек

'''

duraction = 680
sec = duraction % 60
mmin = (duraction - duraction // 3600 * 3600) // 60
hour = (duraction - duraction // 86400 * 86400) // 3600
dday = duraction // 86400
print("duration = ", duraction)
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
list_time = [duraction // 86400,
             (duraction - duraction // 86400 * 86400) // 3600,
             (duraction - duraction // 3600 * 3600) // 60,
             duraction % 60]
list_messer_time = ["дн", "час", "мин", "сек"]
print("Вывод с помощью списка")
# for el in list_time:
#     el * list_time.index(el)

print(f"{str(list_time[0]) + list_messer_time[0]} "
      f"{str(list_time[1]) + list_messer_time[1]} "
      f"{str(list_time[2]) + list_messer_time[2]} "
      f"{str(list_time[3]) + list_messer_time[3]}")
