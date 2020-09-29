# Homework #4

Homework for the class **'Useful tools'**

Introduction to Python Course - Geekbrains

# List of the tasks

## Task #1

#### Ru

Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. 
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

#### En

Implement a script that should include the function of calculating the employee's salary. A formula must be used in the calculation: (output in hours * rate per hour) + bonus. 
In order to perform the calculation for specific values, a script with parameters must be run.

## Task #2

#### Ru

Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

#### En

The list of numbers is presented. It is necessary to display the elements of the original list whose values are greater than the previous element.

## Task #3

#### Ru

Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.

#### En

For numbers between 20 and 240 find numbers divisible by 20 or 21. It is necessary to solve the task in one line.

## Task #4

#### Ru

Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел, соответствующих требованию. 
Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.

#### En

The list of numbers is presented. Identify list items that do not have repetitions. Generate a summary array of numbers that meet the requirement. 
Output the elements in the order in which they appear in the original list. Be sure to use a generator to complete the task.

## Task #5

#### Ru

Реализовать формирование списка, используя функцию ```range()``` и возможности генератора. В список должны войти четные числа от 100 до 1000 (включая границы). 
Необходимо получить результат вычисления произведения всех элементов списка.

#### En

Implement list formation using the ```range()``` function and generator capabilities. The list should include even numbers from 100 to 1000 (including borders). 
The result of calculating the work of all list elements must be obtained.

## Task #6

#### Ru

Реализовать два небольших скрипта:

а) итератор, генерирующий целые числа, начиная с указанного,

б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию ```count()``` и ```cycle()``` модуля ```itertools```. Обратите внимание, что создаваемый цикл не должен быть бесконечным. 
Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. 
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

#### En

Implementation of two small scripts:

a) an iterator that generates integers starting with the specified number,

b) an iterator, repeating the elements of a certain list defined in advance.

Tip: use the ```count()``` and ```cycle()``` functions of the itertools module. Note that the cycle created must not be infinite. 
There must be a condition for its completion.

For example, in the first task, we print integers starting with 3, and when the number 10 is reached, we end the cycle. 
The second task also needs to stipulate the condition that the repetition of list elements will be terminated.

## Task #7

#### Ru

Реализовать генератор с помощью функции с ключевым словом ```yield```, создающим очередное значение. При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: ```for el in fact(n)```. 
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые ```n``` чисел, начиная с ```1!``` и до ```n!```.

#### En

Implement the generator using a function with the keyword yield that creates the next value. When the function is called, a generator object must be created. The function must be called as follows: ```for el in fact(n)```. 
The function is responsible for obtaining the factorial of a number, and only the first ```n``` numbers starting with ```1!``` and ending with ```n!``` must be printed in the loop.

## Contributing

Pull requests are welcome.

## Source

[Geekbrains](https://geekbrains.ru)
