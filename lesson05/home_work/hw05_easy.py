# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import shutil       # Модуль работа с файлами
import re

def create(number=10):
    try:
        for n in range(number):
            os.mkdir('dir_{}'.format(n))
    except OSError:
        print('Такие папки уже существуют')

def remove(number=10):
    try:
        for n in range(number):
            os.rmdir('dir_{}'.format(n))
    except OSError:
        print('Не существует таких папок')
#create()
#remove()
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir():
    print([dir_x for dir_x in os.listdir() if re.search('^[А-Яа-яA-Za-z0-9-_]*$', dir_x)])

#list_dir()
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file(perfix):
    shutil.copyfile('{}/hw05_easy.py'.format(os.getcwd()), '{}/hw05_easy_{}.py'.format(os.getcwd(), perfix))

#copy_file('Bug')
# Функции

def view_content(path='.'):
    if not os.listdir(path) == []:
        print(os.listdir(path))
    else:
        print('Нет содержимого')

def go_to_folder(path, name_dir):
    return os.path.join(path, name_dir)

def remove_dir(path, name_dir):
    os.rmdir('{}/{}'.format(path, name_dir))

def create_dir(path, name_dir):
    os.mkdir('{}/{}'.format(path, name_dir))

def list_dir(path, name_dir):
    for dir_x in os.listdir(path):
        if re.search('^[А-Яа-яA-Za-z0-9-_]*$', dir_x):
            if dir_x == name_dir:
                return True
