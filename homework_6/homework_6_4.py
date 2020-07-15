# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.

# Defining the first class - Car
class Car:

    # Defining the init function
    def __init__(self, _speed, _colour, _name, _police):
        self._speed = _speed
        self._colour = _colour
        self._name = _name
        self._police = _police

    # Defining the functions for performance
    def go(self):
        return f'{self._name} has started'

    def stop(self):
        return f'{self._name} has stopped'

    def turn_right(self):
        return f'{self._name} has turned right'

    def turn_left(self):
        return f'{self._name} has turned left'

    def speed(self):
        return f'The speed of {self._name} is {self._speed}'


# Defining the second class - TownCar
class TownCar(Car):

    # Defining the init function
    def __init__(self, _speed, _colour, _name, _police):
        super().__init__(_speed, _colour, _name, _police)

    # Defining the speed function
    def speed(self):
        print(f'The speed of the town car {self._name} is {self._speed}')

        if self._speed > 60:
            return f'The speed of {self._name} is higher than allowed for this type of car'
        else:
            return f'The speed of {self._name} is okay for this type of car'


# Defining the third class - SportCar
class SportCar(Car):

    # Defining the init function
    def __init__(self, _speed, _colour, _name, _police):
        super().__init__(_speed, _colour, _name, _police)


# Defining the third class - WorkCar
class WorkCar(Car):

    # Defining the init function
    def __init__(self, _speed, _colour, _name, _police):
        super().__init__(_speed, _colour, _name, _police)

    # Defining the speed function
    def speed(self):
        print(f'Current speed of this car {self._name} is {self._speed}')

        if self._speed > 40:
            return f'The speed of {self._name} is higher than allowed for this type of car'


# Defining the third class - PoliceCar
class PoliceCar(Car):

    # Defining the init function
    def __init__(self, _speed, _colour, _name, _police):
        super().__init__(_speed, _colour, _name, _police)

    # Defining the police function
    def police(self):
        if self._police:
            return f'{self._name} is from police, run!'
        else:
            return f'{self._name} is not from the police..'


# Creating the values for further check
BMW = SportCar(120, 'Blue', 'BMW', False)
Toyota = TownCar(35, 'Grey', 'Toyota', False)
Nissan = WorkCar(75, 'Rose', 'Nissan', False)
Lada = PoliceCar(90, 'Blue', 'Lada', True)

# Checking if everything works
print(Nissan.turn_left())
print(f'When {Toyota.turn_right()}, {BMW.stop()} should stop')
print(f'{Nissan.go()} has the speed of {Nissan._speed()}')
print(f'{Nissan._name} is coloured {Nissan._colour}')
print(f'Is {BMW._name} a police car? {BMW._police}')
print(f'Is {Nissan._name}  a police car? {Nissan._police}')
