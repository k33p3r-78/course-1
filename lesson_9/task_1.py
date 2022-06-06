import itertools
import time


class TrafficLight:

    def __init__(self, red_time, yellow_time, green_time):
        self.__color = 'красный'
        self._color_sleep = {
            'красный': red_time,
            'жёлтый': yellow_time,
            'зелёный': green_time
        }

    def state(self):
        return self.__color

    def running(self):
        color_queue = itertools.cycle(['красный', 'жёлтый', 'зелёный', 'жёлтый'])
        for color in color_queue:
            self.__color = color
            print(self.state())
            try:
                time.sleep(self._color_sleep[color])
            except KeyboardInterrupt:
                print('Прервано пользователем')
                break


if __name__ == '__main__':
    t = TrafficLight(5, 3, 6)
    t.running()
