# Homework #6 :atom:

Homework for the class **'Object-oriented programming'**

Introduction to Python Course - Geekbrains

# List of the tasks

## Task #1

#### Ru

Создать класс ```TrafficLight``` (светофор) и определить у него один атрибут ```color``` (цвет) и метод ```running``` (запуск). 
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. 
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. 
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

#### En

Create a class ``` TrafficLight``` (traffic lights) and define one attribute ```color``` (color) and method ```running``` (launch). 
The attribute is implemented as private. Within the method implement switching of traffic lights to the following modes: red, yellow, green. 
The duration of the first state (red) is 7 seconds, the second (yellow) - 2 seconds, the third (green) - at your discretion. 
You may switch between the modes only in the specified order (red, yellow, green). Check the example work by creating an instance and calling the described method.

The task may be complicated by checking the order of the modes and, if it is violated, output the corresponding message and finish the script.

## Task #2

#### Ru

Реализовать класс ```Road``` (дорога), в котором определить атрибуты: ```length``` (длина), ```width``` (ширина). 
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. 
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. 
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чиcло см толщины полотна. 
Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т

#### En

Implement class ```Road``` (road) where you define attributes: ```Length``` (length), ```width``` (width). 
Values of these attributes shall be passed at creation of an instance of the class. Make the attributes protected. 
Determine method of asphalt mass calculation required to cover the whole road surface. 
Use the formula: length * width * mass of asphalt to cover one square meter of the road with 1 cm thick asphalt * number of cm of thickness of the roadbed. 
Check the operation of the method.

For example: 20m * 5000m * 25kg * 5cm = 12500t

## Task #3

#### Ru

Реализовать базовый класс ```Worker``` (работник), в котором определить атрибуты: ```name```, ```surname```, ```position``` (должность), ```income``` (доход). 
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, ```{"wage": wage, "bonus": bonus}```. 
Создать класс ```Position``` (должность) на базе класса ```Worker```. В классе Position реализовать методы получения полного имени сотрудника (```get_full_name```) и дохода с учетом премии (```get_total_income```). 
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

#### En

Implement the basic class ```Worker``` (employee), in which attributes are defined: ```name```, ```surname```, ```position``` (position), ```income``` (income). 
The last attribute must be protected and refer to a dictionary containing elements: salary and bonus, for example, ```{"wage": salary, `"bonus": bonus}```. 
Create a class ```Position``` (position) based on the class ```Worker```. In the Position class, implement methods to obtain the full name of the employee (```get_full_name```) and the income including the bonus (```get_total_income```). 
Check the example work on real data (create instances of Position class, transfer data, check attribute values, call instance methods).

## Task #4

#### Ru

Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: ```speed```, ```color```, ```name```, ```is_police``` (булево). 
А также методы: ```go```, ```stop```, ```turn(direction)```, которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: ```TownCar```, ```SportCar```, ```WorkCar```, ```PoliceCar```. Добавьте в базовый класс метод ```show_speed```, который должен показывать текущую скорость автомобиля. 
Для классов ```TownCar``` и ```WorkCar``` переопределите метод ```show_speed```. При значении скорости свыше 60 (```TownCar```) и 40 (```WorkCar```) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

#### En

Implement the base class Car. This class must have the following attributes: ```speed```, ```color```, ```name```, ```is_police``` (Boolean). 
And also methods: ```go```, ```stop```, ```turn(direction)```, which should inform that the car went, stopped, turned (where). 
Describe some child classes: ```TownCar```, ```SportCar```, ```WorkCar```, ```PoliceCar```. Add to the base class the method ```show_speed```, which should show the current speed of the car. 
For classes ```TownCar``` and ```WorkCar``` redefine the method ```show_speed```. If the speed exceeds 60 (```TownCar```) and 40 (```WorkCar```), the message about speeding should be displayed.

Create class instances, pass attribute values. Perform attribute access, print the result. Execute a method call and also display the result.

## Task #5

#### Ru

Реализовать класс ```Stationery``` (канцелярская принадлежность). Определить в нем атрибут ```title``` (название) и метод ```draw``` (отрисовка). 
Метод выводит сообщение ```“Запуск отрисовки.”``` Создать три дочерних класса ```Pen``` (ручка), ```Pencil``` (карандаш), ```Handle``` (маркер). 
В каждом из классов реализовать переопределение метода ```draw```. Для каждого из классов методы должен выводить уникальное сообщение. 
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

#### En

To implement the class ```Stationery``` (office supplies). Determine the attribute ```title``` (name) and method ```draw``` (drawing) in it. 
The method displays a message ```Start drawing```. Create three child classes ```Pen``` (pen), ```Pencil``` (pencil), ```Handle``` (marker). 
In each class, implement an override of the ```draw``` method. For each of the classes, the methods should display a unique message. 
Create class instances and check what the described method will print for each instance.

## Contributing

Pull requests are welcome.

## Source

[Geekbrains](https://geekbrains.ru)
