# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В
# классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (
# get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

# Defining the first class - Worker
class Worker:

    # Defining the init function
    def __init__(self, _name, _surname, _position, _salary, _bonus):
        self._name = _name
        self._surname = _surname
        self._position = _position
        self._income = {'salary': _salary, 'bonus': _bonus}

    def position(self):
        return self._position


# Defining the second class - Position
class Position(Worker):

    # Defining the init function
    def __init__(self, _name, _surname, _position, _salary, _bonus):
        super().__init__(_name, _surname, _position, _salary, _bonus)

    # Defining the name function
    def name(self):
        return self._name + ' ' + self._surname

    # Defining the income function
    def income(self):
        return self._income.get('salary') + self._income.get('bonus')


# Checking if everything works
result = Position('Ivan', 'Man', 'Postman', '10000', '100')
print(result.name())
print(result.position())
print(result.income())
