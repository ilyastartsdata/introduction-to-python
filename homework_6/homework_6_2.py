# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
# расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина *
# масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
# Проверить работу метода.
#
# Например: 20м * 5000м * 25кг * 5см = 12500 т

# Defining the first class - Road
class Road:

    # Defining the init function
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    # Defining the measurement function - mass
    def measurement_mass(self):
        return self._length * self._width


# Defining the second class - Calculation
class Calculation(Road):

    # Defining the init function
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume


# Checking if everything runs
result = Calculation(25, 10000, 125)
print(result.measurement_mass())
