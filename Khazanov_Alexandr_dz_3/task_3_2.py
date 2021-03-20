'''Доработать предыдущую функцию в num_translate_adv():
реализовать корректную работу с числительными, начинающимися с заглавной буквы —
результат тоже должен быть с заглавной.

'''


def num_translate_adv(engl_num):
    '''Функция переводит числительные от 0 до 10 с английского на русский.
    Учитывается регистр только первой буквы .
    :param engl_num: английское слово для перевода
    :return: русское слово, либо None

    '''
    translate_dict = \
        {'one': 'один',
         'two': 'два',
         'three': 'три',
         'four': 'четыре',
         'five': 'пять',
         'six': 'шесть',
         'seven': 'семь',
         'eight': 'восемь',
         'nine': 'девять',
         'ten': 'десять',
         'zero': 'ноль', }
    modify_engl_num = translate_dict.get(engl_num.lower())
    if engl_num[0].istitle():
        return modify_engl_num.capitalize()
    else:
        return modify_engl_num


print("four -", num_translate_adv("four"))
print("Four -", num_translate_adv("Four"))
print("FOUR -", num_translate_adv("FOUR"))
print("fOUR -", num_translate_adv("fOUR"))
print("f -", num_translate_adv("f"))
