from abc import ABC, abstractmethod


class Clothes(ABC):

    _cloth_spent = 0
    _s_clothe_spent = 0
    _c_cloth_spent = 0

    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def cloth_require(self):
        pass

    @property
    def cloth_spent(self):
        return self._cloth_spent


class Coat(Clothes):


    def __init__(self, size, name='coat'):
        self._size = size
        super().__init__(name)

    @property
    def cloth_require(self):
        return self._size / 6.5 + 0.5

    @property
    def coat_cloth_spent(self):
        return self._c_cloth_spent

    def add_to_reserve(self):
        Clothes._cloth_spent += self.cloth_require
        Clothes._c_cloth_spent += self.cloth_require

class Suit(Clothes):


    def __init__(self, growth, name='suit'):
        self._growth = growth
        super().__init__(name)

    @property
    def cloth_require(self):
        return self._growth * 2 + 0.3

    @property
    def suit_cloth_spent(self):
        return self._s_clothe_spent

    def add_to_reserve(self):
        Clothes._cloth_spent += self.cloth_require
        Clothes._s_clothe_spent += self.cloth_require


if __name__ == '__main__':
    c1 = Coat(48)
    c2 = Coat(12)
    c3 = Coat(60)
    s1 = Suit(180)
    s2 = Suit(60)
    s3 = Suit(158)

    c1.add_to_reserve()
    print(f'Потрачено такни на {c1.name}: {c1.cloth_require}')
    c2.add_to_reserve()
    print(f'Потрачено такни на {c2.name}: {c2.cloth_require}')
    c3.add_to_reserve()
    print(f'Потрачено такни на {c3.name}: {c3.cloth_require}')
    s1.add_to_reserve()
    print(f'Потрачено такни на {s1.name}: {s1.cloth_require}')
    s2.add_to_reserve()
    print(f'Потрачено такни на {s2.name}: {s2.cloth_require}')
    s3.add_to_reserve()
    print(f'Потрачено такни на {s3.name}: {s3.cloth_require}')

    print(f'Всего потрачено ткани: {c1.cloth_spent}')
    print(f'На пальто: {c1.coat_cloth_spent}')
    print(f'На костюмы: {s1.suit_cloth_spent}')
