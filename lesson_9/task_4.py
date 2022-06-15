class Car:

    speed_limits = {
        'TownCar': 60,
        'WorkCar': 40
    }

    def __init__(self, name, color, is_police=False):
        self.name = name
        self.color = color
        self._speed = 0
        self._is_police = is_police

    def go(self):
        self._speed += 20
        print('Машина разгоняется')

    def stop(self):
        self._speed = 0
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость: {self._speed} км/ч')


class TownCar(Car):

    def show_speed(self):
        if self._speed > Car.speed_limits[type(self).__name__]:
            print(f'Вы превысили скорость. Ограничение: {Car.speed_limits[type(self).__name__]} км/ч. Ваша скорость: {self._speed}')
        else:
            super().show_speed()


class WorkCar(Car):

    def show_speed(self):
        if self._speed > Car.speed_limits[type(self).__name__]:
            print(f'Вы превысили скорость. Ограничение: {Car.speed_limits[type(self).__name__]} км/ч. Ваша скорость: {self._speed}')
        else:
            super().show_speed()


class SportCar(Car):

    def go(self):
        self._speed += 20
        super().go()


class PoliceCar(Car):

    def __init__(self, name, color, is_police=True):
        super().__init__(name, color, is_police)






if __name__ == '__main__':
    t_car = TownCar('lincoln', 'серый')
    w_car = WorkCar('КАМАЗ', 'жёлтый')
    s_car = SportCar('lotus', 'черный')
    p_car = PoliceCar('chevrolet', 'служебный')

    print(f'{t_car.color} {t_car.name}:')
    for _ in range(4):
        t_car.go()
    t_car.show_speed()
    t_car.stop()
    print()

    print(f'{w_car.color} {w_car.name}:')
    for _ in range(3):
        w_car.go()
    w_car.show_speed()
    w_car.turn('на право')
    w_car.stop()
    print()

    print(f'{s_car.color} {s_car.name}:')
    for _ in range(3):
        s_car.go()
    s_car.show_speed()
    s_car.stop()
    print()

    print(f'{p_car.color} {p_car.name}:')
    if p_car._is_police:
        print('Машина оборудована полицейским оснащением')



