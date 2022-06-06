class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_flow(self, mass_to_cover, height):
        res = round(self._width*self._length*mass_to_cover*height/1000)
        return f'{self._length}м * {self._width}м * {mass_to_cover}кг * ' +\
               f'{height}см = {res}т'


if __name__ == '__main__':
    r = Road(5000, 20)
    print(r.calculate_flow(25, 5))
    r2 = Road(11000, 15)
    print(r2.calculate_flow(25, 7))
