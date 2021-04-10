"""аписать скрипт, создающий из config.yaml
стартер для проекта со следующей структурой:
Примечание: структуру файла config.yaml придумайте сами

структура config.yaml:
дефис показывает уровень вложенности
крышка - файл, нет крышки - папка
"""


def type_str(line_str: str):
    """
    удаление из строки дефисов и крышки
    :param line_str: строка
    :return: обработанная строка;
    признак: f - имя файла, d - имя каталога;
     уровень вложенности
    """
    level = line_str.count('-')
    if line_str[0] == '^':
        line_str = line_str.replace('^', '').replace('-', '')[:-1]
        return line_str, 'f', level
    else:
        line_str = line_str.replace('-', '')[:-1]
        return line_str, 'd', level


import os
level = 0
level_path = ".\\"
print("Создание структуры проекта из config.yaml в", os.path.abspath(level_path))

with open('config.yaml', encoding='utf-8') as f:
    for line in f:
        line, sign, line_level = type_str(line)
        different = line_level - level
        if different < 0:
            if sign == 'f':
                for d in range(abs(different)):
                    path_file_level = os.path.dirname(os.path.abspath(path_file))
                path_file = os.path.join(path_file_level, line)
                if os.path.exists(path_file):
                    print("Файл", line, "существует, исправьте шаблон")
                    exit()
                else:
                    ff = open(path_file, 'w', encoding='utf-8')
                    ff.close()
                # print(line, "file - level", level, path_file)
            else:
                for d in range(abs(different)):
                    level_path = os.path.dirname(os.path.abspath(level_path))
                level_path = os.path.join(level_path, line)
                if os.path.isdir(level_path):
                    level_path = os.path.dirname(level_path)
                else:
                    os.mkdir(level_path)
                # print(line, "dir - level", level, level_path)
        else:
            level = line_level
            if sign == 'f':
                path_file = os.path.join(level_path, line)
                if os.path.exists(path_file):
                    print("Файл", line, "существует, исправьте шаблон")
                    exit()
                else:
                    ff = open(path_file, 'w', encoding='utf-8')
                    ff.close()
                # print(line, "file - level", level, path_file)
            else:
                level_path = os.path.join(os.path.abspath(level_path), line)
                if os.path.isdir(level_path):
                    print("Каталог", line, "существует, исправьте шаблон")
                else:
                    os.mkdir(level_path)
                # print(line, "dir - level", level, level_path)