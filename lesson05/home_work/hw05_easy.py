# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import shutil
import re

print('-' * 5, 'Решение первой задачи', '-' * 5)

try:
    for n in range(9):
        os.mkdir('dir_{}'.format(n + 1))
except OSError:
    print('Такие папки уже существуют')

input('Папки создались')

try:
    for n in range(9):
        os.rmdir('dir_{}'.format(n + 1))
except OSError:
    print('Не существует таких папок')

print('Папки удалились')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
print('-' * 5, 'Решение второй задачи', '-' * 5)

print([dir_x for dir_x in os.listdir() if re.search('^[А-Яа-яA-Za-z0-9-_]*$', dir_x)])

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

print('-' * 5, 'Решение третий задачи', '-' * 5)

shutil.copyfile('{}/hw05_easy.py'.format(os.getcwd()), '{}/hw05_easy_copy.py'.format(os.getcwd()))
