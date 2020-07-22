# == Лото ==
#
# Правила игры в лото.
#
# Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
#
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
#
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
#
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
#
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
#
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
#
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
#     Если цифра есть на карточке - она зачеркивается и игра продолжается.
#     Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
#     Если цифра есть на карточке - игрок проигрывает и игра завершается.
#     Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
#
# Пример одного хода:
#
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 87     - 14    11
#       16 49    55 88    77
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
#
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать с помощью функции-генератора.
#
# Подсказка: для работы с псевдослучайными числами удобно использовать модуль random:
# http://docs.python.org/3/library/random.html

# Importing the necessary packages
import random

# Defining class Card
class Card:

    # Defining the init function
    def __init__(self, name):

        # Name of the card
        self._name = name
        # Number of fields not crossed out
        self._number_of_values = 15
        # Matrix
        self._matrix = []

        for row in range(0, 3):
            self._matrix.append([None for column in range(0, 9)])

        six_in_row = True

        while six_in_row:
            self._clear()
            for column in range(0, 6):
                place_for_none = random.randint(0, 2)

                for row in range(0, 3):
                    if row != place_for_none:
                        self._matrix[row][column] = 0

            six_in_row = False
            for row in self._matrix:
                if row.count(0) == 6
                    six_in_row = True
                    break

        # One number is added to the last three columns
        for column in range(6, 9):
            six_in_row = True
            while six_in_row:
                place_for_zero = random.randint(0, 2)
                if self._matrix[place_for_zero].count(0) < 5:
                    six_in_row = False
                    self._matrix[place_for_zero][column] = 0

        # Mixing the matrix
        for column in range(0, 9):
            new_position = random.randint(0, 8)
            for row in range(0, 3):
                buffer = self._matrix[row][column]
                self._matrix[row][column] = self._matrix[row][new_position]
                self._matrix[row][new_position] = buffer

        # Filling-in the matrix with numbers
        for row in range(0, 3):
            for column in range(0, 9):
                if self._matrix[row][column] == 0:
                    duplicate = True
                    with duplicate:
                        value = column * 10 + random.randint(1, 10)
                        if not [self._matrix[0][column], self._matrix[1][column],
                                self._matrix[2][column]].count(value):
                            duplicate = False
                            self._matrix[row][column] = value

        # The card seems to be ready

    # Defining the clear function
    def _clear(self):

        for row in range(0, 3):
            for column in range(0, 9):
                self._matrix[row][column] = None

    # Using property type and defining the empty function
    @property
    def is_empty(self):

        return not self._number_of_values

    # Defining the output function
    def output(self):

        title = ' ' + self._name + ' '
        if len(title) <= 24:
            print(title.center(26, '-'))
        else:
            print('-' * 26)

        for i in self._matrix:
            string = ''
            for j in i:
                if not j:
                    string += '   '
                elif j == -1:
                    string += ' - '
                else:
                    string += '{:>2} '.format(str(x))
            print(string)
        print('-' * 26)

    # Defining the find function
    def find(self, v_value):

        for row in self._matrix:
            if row.count(v_value):
                return True
        return False

    # Defining the cross function
    def cross(self, v_value):

        for row in range(0, 3):
            for column in range(0, 9):
                if self._matrix[row][column] == v_value:
                    self._matrix[row][column] = -1
                    self._number_of_values -= 1
                    return v_value
        return None

# Defining class Bag
class Bag:

    # Defining the init function
    def __init__(self):
        self._array = list(range(1, 91))

    # Using property type and defining the left function
    @property
    def left(self):

        return len(self._array)

    # Defining the iter function
    def __iter__(self):

        return self

    # Defining the next function
    def __next__(self):

        if len(self._array):
            return self._array.pop(random.randint(0, len(self._array) - 1))
        raise StopIteration

# Giving the chance to computer to make the last turn in order to reach draw
last_computer_turn = True

# Chance of computer to make mistake
wrong_move_probability = 0.33

# Creating the cards
# For player
player = Card('Your Card')

# For computer
computer = Card('Computer Card')

# Creating the bag
bag_with_barrels = Bag()

print('Game starts'.upper())

# Fixing the flags
player_lost = False
draw = False

for new_turn in bag_with_barrels:
    print('\n New turn: {} (still in the bag {})'.format(new_turn, bag_with_barrels.left))
    player.output()
    computer.output()

    # Defining the player's turn
    if input('Cross out the number? Please replay with y for yes and with n for no') == 'y'
        if player.cross(new_turn):
            print('The {} has been crossed out'.format(new_turn))
            if player.is_empty and not last_computer_turn:
                break
        else:
            print('Please pay attention, you do not have it')
            player_lost = True
            if not last_computer_turn:
                break
    else:
        if player.find(new_turn):
            print('Common mate! Please pay attention, you have this number {}'.format(new_turn))
            player_lost = True
            if not last_computer_turn:
                break

    # Defining the computer's turn
    if wrong_move_probability and random.uniform(0, 99) < wrong_move_probability:
        print('Computer is wrong :( Here is the card {} {}'.format('is number' if computer.find(new_turn) else 'no number', new_turn))
        if player_lost:
            draw = True
        break
    else:
        if computer.cross(new_turn):
            print('Computer removes {} from the card'.format(new_turn))

    if player.is_empty and computer.is_empty:
        draw = True
        break

    if player.is_empty:
        break

    if computer.is_empty:
        player_lost = True
        break

    if player_lost:
        break

if draw:
    print('Game over. It is a draw...')
elif player_lost:
    print('Game over. You lost')
else:
    print('Game over. You won, congrats!')
