class Complex:


    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f'{self._x}{self._y:+0d}j'

    def __add__(self, other):
        return Complex(self._x + other._x, self._y + other._y)

    def __sub__(self, other):
        return Complex(self._x - other._x, self._y - other._y)

    def __mul__(self, other):
        return Complex(self._x * other._x - self._y * other._y, \
                        self._y * other._x + self._x * other._y)


if __name__ == '__main__':
    c1 = Complex(2,3)
    c2 = Complex(-1,1)
    print(f'Число 1: {c1}')
    print(f'Число 2: {c2}')
    print(f'Сложение: {c1+c2} {type(c1+c2)}')
    print(f'Вычитание: {c1-c2} {type(c1-c2)}')
    print(f'Умножение: {c1*c2} {type(c1*c2)}')










