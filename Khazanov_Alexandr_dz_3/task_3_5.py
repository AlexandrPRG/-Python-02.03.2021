'''Реализовать функцию get_jokes(), возвращающую n шуток,
сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого).
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий
повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)?
Сможете ли вы сделать аргументы именованными?
'''


def get_jokes(n, repeat=False):
    '''возвращает n шуток из трех списков
    :param n: количество шуток
    :param repeat: флаг включения/выключения повторов слов в шутках
    по умолчанию выключен, то есть повтор слов не обрабатывается
    :return: n-строк с n-шуток
    '''

    import random
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    str_out = ""  # вывод шуток
    if bool(repeat):  # переключатель повторения слов
        nouns_was = []  # список уже бывших слов
        adverbs_was = []  # то же
        adjectives_was = []  # то же
        for i in range(n):
            str_joke = []  # шутка
            # удаление уже использованных слов
            list_filter_nouns = list(set(nouns).difference(set(nouns_was)))
            list_filter_adverbs = list(set(adverbs).difference(set(adverbs_was)))
            list_filter_adjectives = list(set(adjectives).difference(set(adjectives_was)))
            # если есть слова в списках, получение рандомизированного слова
            if len(list_filter_nouns) or len(list_filter_adverbs) or len(list_filter_adjectives):
                new_word_noun = random.choice(list_filter_nouns)
                new_word_adverb = random.choice(list_filter_adverbs)
                new_word_adjective = random.choice(list_filter_adjectives)
                # добавление слова в список использованных
                nouns_was.append(new_word_noun)
                adverbs_was.append(new_word_adverb)
                adjectives_was.append(new_word_adjective)
                # формирование шутки и вывода
                str_joke.append(new_word_noun)
                str_joke.append(new_word_adverb)
                str_joke.append(new_word_adjective)  # строка шутки
                str_out = str_out + " ".join(str_joke) + "\n"  # строки n-шуток
            # если слов не осталось
            else:
                str_out = str_out + "Шутки кончились\n"
    else:
        for i in range(n):
            str_joke = f"{random.choice(nouns)} " \
                       f"{random.choice(adverbs)} " \
                       f"{random.choice(adjectives)}"  # строка шутки
            str_out = str_out + str_joke + "\n"  # строки n-шуток
    return str_out


print(get_jokes(4, 1))
