"""
2.	Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
a.	Вычислить сумму тех чисел из этого списка,
 сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859»
 будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
 Внимание: использовать только арифметические операции!
b.	К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел
 из этого списка, сумма цифр которых делится нацело на 7.
c.	* Решить задачу под пунктом b, не создавая новый список.

"""
list_cub = [n ** 3 for n in range(1, 1000, 2)] #список, состоящий из кубов нечётных чисел
print("Список кубов нечётных чисел")
print(list_cub)
# a
sum_number7 = 0 # сумма тех чисел списка, сумма цифр которых делится нацело на 7
for el in list_cub:
    sum_digit_el = 0 # сумма цифр элемента списка
    item = el
    while el:
        digit = el % 10 # цифра элемента списка
        sum_digit_el += digit
        el = el // 10
    if sum_digit_el % 7 == 0:
        sum_number7 += item
print("Сумма тех чисел списка, сумма цифр которых делится нацело на 7 =", sum_number7)
# b
list_cub17 = []
for el in list_cub: # добавить     17 вычислить то же
    list_cub17.append(el + 17)
print("Список кубов нечётных чисел + 17")
print(list_cub17)
sum_number7 = 0 # сумма тех чисел списка, сумма цифр которых делится нацело на 7
for el in list_cub17:
    sum_digit_el = 0 # сумма цифр элемента списка
    item = el
    while el != 0:
        digit = el % 10 # цифра элемента списка
        sum_digit_el += digit
        el = el // 10
    if sum_digit_el % 7 == 0:
        sum_number7 += item
print("Сумма тех чисел списка, сумма цифр которых делится нацело на 7 =", sum_number7)
# c
for i in range(len(list_cub)): # модификация списка (el+17)
    el = list_cub[i]
    list_cub.pop(i)
    list_cub.insert(i, el + 17)
print("Список кубов нечётных чисел модифицированный")
print(list_cub)
