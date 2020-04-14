# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
# color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
# скорости.

class Car():
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def to_go(self):
        print('Машина двинулась с места.')

    def to_stop(self):
        print('Машина остановилась.')

    def to_turn_left(self):
        print('Машина повернула налево.')

    def to_turn_right(self):
        print('Машина повернула направо.')

    def show_speed(self):
        print(f'Машина движется со коростью {self.speed} км/ч.')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print('Вы превышаете скорость')
        else:
            print(f'Машина движется со коростью {self.speed} км/ч.')


class SportCar(Car):

    def show_car(self):
        print('Это спортивная машина')


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print('Вы превышаете скорость')
        else:
            print(f'Машина движется со коростью {self.speed} км/ч.')


class PoliceCar(Car):

    def show_car(self):
        print('Это полицейская машина машина')


# sc = SportCar(120, 'green', 'mazda')
# sc.show_speed()
tc = TownCar(61, 'red', 'town car')
tc.to_stop()
tc.to_go()
tc.to_turn_left()
tc.to_turn_right()
tc.show_speed()

