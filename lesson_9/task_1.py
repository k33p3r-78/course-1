import itertools
import time


class TrafficLight:

    color_sleep = {
        'красный': 7,
        'жёлтый': 2,
        'зелёный': 5
    }

    def __init__(self):
        self.__color = 'красный'

    def state(self):
        return self.__color

    def running(self):
        cd_to_off = 10
        color_queue = itertools.cycle(['красный', 'жёлтый', 'зелёный', 'жёлтый'])
        for color in color_queue:
            self.__color = color
            print(self.state())
            time.sleep(TrafficLight.color_sleep[color])
            cd_to_off -= 1
            if cd_to_off == 0: break


if __name__ == '__main__':
    t = TrafficLight()
    t.running()
