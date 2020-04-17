"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


class Сlothing:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height

    def __str__(self):
        return f'Название изделия: {self.name}\nШирина изделия: {self.width}\nДлина изделия: {self.height}'


class Coat(Сlothing):

    def __init__(self, name, width, height):
        super().__init__(name, width, height)

    @property
    def square(self):
        return f'Необходимо для пошива {int(self.width / 6.5 + 0.5)} см.'


class Costume(Сlothing):

    def __init__(self, name, width, height):
        super().__init__(name, width, height)

    @property
    def square(self):
        return f'Необходимо для пошива {int(2 * self.height + 0.3)} см.'


mc = Coat('Пальто', 30, 40)
print(mc.square)

mco = Costume('Тройка', 20, 20)
print(mco.square)
