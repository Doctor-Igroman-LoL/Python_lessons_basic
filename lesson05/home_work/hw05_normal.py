# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import os

from hw05_easy import go_to_folder
from hw05_easy import view_content
from hw05_easy import remove_dir
from hw05_easy import list_dir
from hw05_easy import create_dir

current_dir = os.getcwd()

if __name__ == '__main__':
    while True:
        try:
            action = int(input('Введите команду: 1. Перейти в папку, 2. Просмотреть содержимое текущей папки, '
                           '3. Удалить папку, 4. Создать папку, 5. Выход: '))
            print('Введина команда: {}'.format(action))
            if action == 1:
                name_dir = input('Введите имя папки: ')
                if list_dir(current_dir, name_dir):
                    current_dir = go_to_folder(current_dir, name_dir)
                    print('Вы успешно перешли по пути: {}'.format(current_dir))
                else:
                    print('Не возможно перейти')
            elif action == 2:
                view_content(current_dir)
            elif action == 3:
                try:
                    name_dir = input('Введите имя папки, которую хотите удалить: ')
                    remove_dir(current_dir, name_dir)
                    print('Вы успешно удалили папку: {}'.format(name_dir))
                except:
                    print('Невозможно удалить. Нет такой папки')
            elif action == 4:
                try:
                    name_dir = input('Введите имя папки, которую хотите создать: ')
                    create_dir(current_dir, name_dir)
                    print('Папка успешна создана: {}'.format(name_dir))
                except:
                    print('Не возможно создать папку')
            elif action == 5:
                break
        except:
            print('Вы вели не верную команду')
