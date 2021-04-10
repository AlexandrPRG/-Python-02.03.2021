"""Написать скрипт, создающий стартер (заготовку)
для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые
 папки уже есть на диске (как быть?);
 как лучше хранить конфигурацию этого стартера,
 чтобы в будущем можно было менять имена папок под конкретный проект;
 можно ли будет при этом расширять конфигурацию и хранить данные
 о вложенных папках и файлах (добавлять детали)?
 starter_list = "my_project",
                "settings",
                "mainapp",
                "adminapp",
                "authapp"


решение с созданием нужного количества папок и
сохранением конфигурации в корневом каталоге проекта в файле configuration.project
"""

import os
starter_list = []
root_actual = ".\\"
print("Создание проекта в", os.path.abspath(root_actual))
dir_project = True
while dir_project:
    dir_project = input("Корневой каталог: ")
    path_project = os.path.abspath(root_actual) + "\\" + dir_project
    if not os.path.exists(dir_project):
        os.mkdir(root_actual + dir_project)
        starter_list.append(str(dir_project))
        break
    else:
        print("Проект", os.path.basename(root_actual + dir_project),
          "уже есть")
        what_do = input("Enter - добавить подпапки, q - завершить ")
        if what_do == "":
            break
        else:
            exit()
sub_dir = True
while sub_dir:
        sub_dir = input("Подкаталог проекта (выход - Enter): ")
        if not os.path.exists(path_project + "\\" + sub_dir):
            # if sub_dir != "":
                starter_list.append(str(sub_dir))
                os.mkdir(path_project + "\\" + sub_dir)
            # else:
            #     sub_dir = False
        else:
            if sub_dir != "":
                print("Каталог существует")
            else:
                sub_dir = False
with open(os.path.join(path_project, "configuration.project"), 'a', encoding='utf-8') as f:
    f.write(dir_project + "\n")
    for itim in starter_list[1:]:
        f.write("\t" + itim + "\n")
