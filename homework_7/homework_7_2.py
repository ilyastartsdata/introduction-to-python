# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У
# этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 +
# 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет
# расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных
# классов проекта, проверить на практике работу декоратора @property.

class Clothers:

    # Defining the init function
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Defining the coat function
    def get_coat(self):
        return self.width / 6.5 + 0.5

    # Defining the jacket function
    def get_jacket(self):
        return self.height * 2 + 0.3

    # Defining the total function
    @property
    def get_total(self):
        return str(f'Total fabric area  \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Clothers):

    # Defining the init function
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    # Defining the str function
    def __str__(self):
        return f'Coat area is {self.square_c}'


class Jacket(Clothers):

    # Defining the init function
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 2 + 0.3)

    # Defining the str function
    def __str__(self):
        return f'Jacket area is {self.square_j}'

# Final check

coat = Coat(3, 5)
jacket = Jacket(3, 5)
print(coat)
print(jacket)
print(coat.get_coat())
print(jacket.get_jacket())
