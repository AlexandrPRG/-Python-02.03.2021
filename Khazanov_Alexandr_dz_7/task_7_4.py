"""Написать скрипт, который выводит статистику для заданной папки
в виде словаря, в котором ключи — верхняя граница размера файла
(пусть будет кратна 10), а значения — общее количество файлов
(в том числе и в подпапках), размер которых не превышает этой границы,
но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""