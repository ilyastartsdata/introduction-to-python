# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

# Defining the first class - Stationary
class Stationary:

    # Defining the init function
    def __init__(self, _title):
        self._title = _title

    # Defining the draw function
    def draw(self):
        return f'Let us check {self._title}'


# Defining the second class - Pen
class Pen(Stationary):

    # Defining the init function
    def __init__(self, _title):
        super().__init__(_title)

    # Defining the draw function
    def draw(self):
        return f'You have taken {self._title}'


# Defining the third class - Pencil
class Pencil(Stationary):

    # Defining the init function
    def __init__(self, _title):
        super().__init__(_title)

    # Defining the draw function
    def draw(self):
        return f'You have picked {self._title}'


# Defining the fourth class - Handle
class Handle(Stationary):

    # Defining the init function
    def __init__(self, title):
        super().__init__(title)

    # Defining the draw function
    def draw(self):
        return f'You have picked {self._title}'


# Checking if everything works
choosing_pen = Pen('Pen')
choosing_pencil = Pencil('Pencil')
choosing_handle = Handle('Handle')
print(choosing_pen.draw())
print(choosing_handle.draw())
print(choosing_pencil.draw())
