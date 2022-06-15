class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def __init__(self):
        self.title = 'ручка'

    def draw(self):
        super().draw()
        print(f'Для рисования используем: {self.title}')


class Pencil(Stationery):

    def __init__(self):
        self.title = 'карандаш'

    def draw(self):
        super().draw()
        print(f'Для рисования используем: {self.title}')


class Handle(Stationery):

    def __init__(self):
        self.title = 'маркер'

    def draw(self):
        super().draw()
        print(f'Для рисования используем: {self.title}')


if __name__ == '__main__':
    st_list = [
        Stationery('перо'),
        Pen(),
        Pencil(),
        Handle()
    ]
    
    for el in st_list:
        el.draw()







