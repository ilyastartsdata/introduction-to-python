# Homework #8 :atom:

Homework for the class **'Object-oriented programming - Useful extras'**

Introduction to Python Course - Geekbrains

# List of the tasks

## Task #1

#### Ru

== Лото ==

Правила игры в лото.

Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

```
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
```

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

```
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
```

#### En

== Loto ==

The rules of the lotto game.

The game is played using special cards with numbers marked on them,
and chips (kegs) with numbers.

The number of kegs is 90 (with numbers from 1 to 90).

Each card contains 3 rows of 9 cells. Each line contains 5 random numbers,
located in ascending order. All numbers on the card are unique. Example card:

```
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
```

The game has 2 players: the user and the computer. Each player is given at the beginning
a random card.

One random barrel is selected for each move and displayed on the screen.
A player card and a computer card are also displayed.

The user is asked to cross out the number on the card or continue.
If the player chooses to "cross out":
    If the number is on the card, it is crossed out and the game continues.
    If there is no number on the card - the player loses and the game ends.
If the player chose "continue":
    If the number is on the card - the player loses and the game ends.
    If there are no numbers on the card - the game continues.

The first one to close all the numbers on his card wins.

An example of one turn:

```
New keg: 70 (76 left).
------ Your card -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
---   Computer card    ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Strike a number? (y/n)
```

## Contributing

Pull requests are welcome.

## Source

[Geekbrains](https://geekbrains.ru)
