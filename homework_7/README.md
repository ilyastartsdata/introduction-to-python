# Homework #7 :atom:

Homework for the class **'Object-oriented programming - Advanced level'**

Introduction to Python Course - Geekbrains

# List of the tasks

## Task #1

#### Ru

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод ```__init__()```), который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода ```__str__()``` для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода ```__add__()``` для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

#### En

Implement the Matrix class (matrix). Ensure that the class constructor (method ```__init__()```) is overloaded and must receive data (list of lists) to form the matrix.
The next step is to implement an overload of the method ```__str__()``` to output the matrix in its usual form.
The next step is to implement the method overload ```__add__()`` to implement the operation of adding two Matrix objects (two matrices). The result of the addition should be a new matrix.

Translated with www.DeepL.com/Translator (free version)

## Task #2

#### Ru

Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. 
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

#### En

Implement a project to calculate total fabric consumption for clothing production. The main essence (class) of this project is clothes that may have a certain name. The types of clothing in this project include coats and suits. 
These types of clothing have parameters: size (for coats) and height (for suits). These can be regular numbers: V and H, respectively.
To determine the fabric consumption for each type of clothing, use the following formulae: for the coat (V/6.5 + 0.5), for the suit (2 * H + 0.3). Check the performance of these methods on real data.

Implement the overall fabric consumption calculation. Check the knowledge gained in this lesson: implement abstract classes for the main classes of the project, check the work of the decorator @property.

## Task #3

#### Ru

Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число). 
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (```__add__()```), вычитание (```__sub__()```), умножение (```__mul__()```), деление (```__truediv__()``).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения до целого числа.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод ```make_order()```, принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.

Метод должен возвращать строку вида ```*****\n*****\n*****...```, где количество ячеек между ```\n``` равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод ```make_order()``` вернет строку: ```*****\n*****\n**```.

Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод ```make_order()``` вернет строку: ```*****\n*****\n*****```.

#### En

Implement the programme of work with organic cells. It is necessary to create a Cell class. In its designer, initialise the parameter corresponding to the number of cells (whole number). 
Methods of overloading arithmetic operators should be implemented in the class: addition (```__add__()```), subtraction (```__sub__()```), multiplication (```__mul__()```), division (```__truediv__()``).
These methods should only be applied to cells and perform magnification, reduction, multiplication and normal (not integer) division of cells, respectively. In the division method, the value must be rounded to the whole number.

Folding. Combination of two cells. The number of cells of a common cell must be equal to the sum of cells of the original two cells.

Subtraction. Two cells are involved. The operation must only be performed if the difference in the number of cells of the two cells is greater than zero, otherwise the corresponding message must be output.

Multiplication. A common cell is created from two cells. The number of cells of a total cell is defined as the product of the number of cells of the two cells.

Dividing. A total cell is created from two cells. The number of cells of a total cell is defined as an integer division of the number of cells of these two cells.

The method ```make_order()``` must be implemented in the class, taking a copy of the class and the number of cells in the row. This method allows organizing cells into rows.

The method must return a line of the view ```*****\n*****\n*****...``` where the number of cells between ```\n``` is equal to the argument passed. If there are not enough cells to form a row, all the remaining cells are written in the last row.

For example, the number of cells in a row is 12 and the number of cells in a row is 5. Then the ```make_order()``` method will return the row: ```*****\n*****\n**```.

Or, the number of cells in a row is 15, the number of cells in a row is 5. Then the method ```make_order()`` will return a line: ```*****\n*****\n*****```.

## Contributing

Pull requests are welcome.

## Source

[Geekbrains](https://geekbrains.ru)
