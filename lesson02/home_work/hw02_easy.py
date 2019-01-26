# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
print('-' * 5, 'Решение первой задачи', '-' * 5)
fruits = ["яблоко", "банан", "киви", "арбуз"]
number = 0
for fruit in fruits:
    number += 1
    print('{0}.  {1:>6}'.format(number, fruit))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

print('-' * 5, 'Решение второй задачи', '-' * 5)
first_list = [1, 8, 3, 5]
second_list = [5, 6, 7, 8]
first_list = set(first_list) - set(second_list)
print(list(first_list))

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
