'''Написать функцию num_translate(), переводящую числительные от 0 до 10
c английского на русский язык. Если перевод сделать невозможно, вернуть None

'''


def num_translate(engl_num):
    '''Функция переводит числительные от 0 до 10 с английского на русский
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
    return translate_dict.get(engl_num)


print("four -", num_translate("four"))
print("f -", num_translate("f"))
