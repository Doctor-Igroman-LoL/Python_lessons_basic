# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
print('-' * 5, 'Решение первой задачи', '-' * 5)

random_list = [23, 64, 45, 49, 169, -25, 3355, 21025, 53, 43, 16]
new_list = []

for number in random_list:
    if number > 0:
        number = number ** 0.5
        point = str(number).find('.')
        result = str(number)[point + 1:]
        if int(result) == 0:
            new_list.append(int(number))
print(str(new_list))


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
print('-' * 5, 'Решение второй задачи', '-' * 5)

hash_days = {'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое', '05': 'пятое', '06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое', '11': 'одиннадцатое', '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое', '15': 'пятнадцатое', '16': 'шестнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое', '21': 'двадцать первое ', '22': 'двадцать второе', '23': 'двадцать третье', '24': 'двадцать четвертое', '25': 'двадцать пятое', '26': 'двадцать шестое', '27': 'двадцать седьмое', '28': 'двадцать восьмое', '29': 'двадцать девятое', '30': 'тридцатое', '31': 'тридцать первое '}
hash_month = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня', '07': 'июля', '08': 'августа', '09': 'сентябре', '10': 'октября', '11': 'ноября', '12': 'декабря'}
date = input('Введите вашу дату рождения в формате dd.mm.yyyy. Например: 02.11.2013: ')
days = date[:2]
month = date[3:5]
yeas = date[6:10]
print('{} {} {} года, вы появились =3'.format(hash_days[days], hash_month[month], yeas))

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
print('-' * 5, 'Решение третий задачи', '-' * 5)

import random

random_ = random.randint(2, 30)
list_random = []
i = 1
while random_ > i:
    list_random.append(random.randint(-100, 100))
    i = i + 1

print(str(list_random))
# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
print('-' * 5, 'Решение четвертой задачи', '-' * 5)

array = [1, 8, 3, 5, 10, 13, 10, 8, 34, 3]
array_copies = set(array)
array_without_copies = set(array) ^ array_copies
print('а) ' + str(list(array_copies)))
print('б) ' + str(list(array_without_copies)))  # ???
