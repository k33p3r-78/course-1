from random import randint


class Cage:


    def __init__(self, cells):
        self._cells = cells

    def make_order(self, cells_in_line):
        res = ''
        last_not_full = False
        lines = self._cells // cells_in_line
        if self._cells // cells_in_line or not lines:
            lines += 1
            last_not_full = True
        for i in range(lines):
            if last_not_full and i == lines-1:
                res += '*' * (self._cells % cells_in_line) + '\n'
            else:
                res += '*' * cells_in_line + '\n'
        return res

    def __add__(self, other):
        if isinstance(other, Cage):
            return Cage(self._cells + other._cells)
        else:
            raise ValueError

    def __sub__(self, other):
        if isinstance(other, Cage) and \
            self._cells - other._cells >= 0:
            return Cage(self._cells - other._cells)
        else:
            raise ValueError

    def __mul__(self, other):
        if isinstance(other, Cage):
            return Cage(self._cells * other._cells)
        else:
            raise ValueError

    def __floordiv__(self, other):
        if isinstance(other, Cage) and other._cells:
            return Cage(self._cells // other._cells)
        else:
            raise ValueError


if __name__ == '__main__':
    cages = []
    for i in range(8):
        cages.append(Cage(randint(1, 66)))
    sum = cages[1] + cages[2]
    sub = cages[3] - cages[4] if cages[3]._cells > cages[4]._cells else cages[4] - cages[3]
    mul = cages[5] * cages[6]
    div = cages[7] // cages[0] if cages[7]._cells > cages[0]._cells else cages[0] - cages[7]
    print(f'Сложение:\n{cages[1].make_order(10)}+\n{cages[2].make_order(10)}=\n{sum.make_order(10)}')
    input('Нажмите Enter для продолжения')
    print(f'Вычитание:\n{cages[3].make_order(10)}-\n{cages[4].make_order(10)}=\n{sub.make_order(10)}')
    input('Нажмите Enter для продолжения')
    print(f'Умножение:\n{cages[5].make_order(10)}*\n{cages[6].make_order(10)}=\n{mul.make_order(10)}')
    input('Нажмите Enter для продолжения')
    print(f'Деление:\n{cages[7].make_order(10)}//\n{cages[0].make_order(10)}=\n{div.make_order(10)}')