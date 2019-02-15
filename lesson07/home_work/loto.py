#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random

class Card:

    def __init__(self):
        self.matrix = [[], [], []]
        self.buffer = 0

    def creation(self):
        self.number_random = random.sample(range(1, 91), 15)
        self.number_random.sort()
        for i, line in enumerate(self.number_random):
            if i in range(0, 5):
                self.matrix[0].append(line)
            elif i in range(5, 10):
                self.matrix[1].append(line)
            elif i in range(10, 15):
                self.matrix[2].append(line)
        for i in range(4):
            self.matrix[0].insert(random.randint(1, 4), ' ')
            self.matrix[1].insert(random.randint(1, 9), ' ')
            self.matrix[2].insert(random.randint(1, 9), ' ')

class MyCard(Card):

    def cross_out(self, number, action):
        if action == 'y':
            for i, line in enumerate(self.matrix):
                self.buffer += 1
                if number in line:
                    for index, n in enumerate(line):
                        if str(n) == str(number):
                            line[index] = '-'
                            return False
                elif self.buffer == 3:
                    self.buffer = 0
                    return True
        elif action == 'n':
            for i, line in enumerate(self.matrix):
                self.buffer += 1
                if number in line:
                    for index, n in enumerate(line):
                        if str(n) == str(number):
                            return True
                elif self.buffer == 3:
                    self.buffer = 0
                    return False
        else:
            return True

    def display(self):
        print('-' * 9, 'Ваша карточка', '-' * 10)
        print('\n'.join('\t'.join(map(str, row))
                         for row in self.matrix))
        print('-' * 34)

class ComCard(Card):

    def cross_out(self, number, action='Bug'):
        for i, line in enumerate(self.matrix):
            for index, n in enumerate(line):
                if str(n) == str(number):
                    line[index] = '-'

    def display(self):
        print('-' * 6, 'Карточка компьютера', '-' * 7)
        print('\n'.join('\t'.join(map(str, row))
                         for row in self.matrix))
        print('-' * 34)

class KegEngine:

    def __init__(self):
        self.excluding_kegs = []
        self.keg = 0

    def random_keg(self):
        while True:
            self.keg = random.randrange(1, 91)
            if not self.keg in self.excluding_kegs:
                self.excluding_kegs.append(self.keg)
                break

    def display_keg(self):
        return self.keg

    def display_balance(self):
        return 90 - len(self.excluding_kegs)

    def display(self):
        print('Новый бочонок: {} (осталось {})'.format(self.display_keg(), self.display_balance()))

class GameEngine:

    def __init__(self):
        self.player = MyCard()
        self.comp = ComCard()
        self.keg = KegEngine()
        self.action = False
        self.card_generation()
        self.exit = False

    def card_generation(self):
        self.player.creation()
        self.comp.creation()

    def display(self):
        self.keg.random_keg()
        self.keg.display()
        self.player.display()
        self.comp.display()

    def run(self):
        while True:

            self.display()
            self.action = input('Зачеркнуть цифру? (y/n) ')
            self.comp.cross_out(self.keg.keg)
            self.exit = self.player.cross_out(self.keg.keg, self.action)
            if self.exit:
                break

game = GameEngine()
game.run()

