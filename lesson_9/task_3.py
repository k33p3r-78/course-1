class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            'wage': wage,
            'bonus': bonus
        }


class Position(Worker):

    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        # Класс Position является наследником Worker
        # Поэтому обращаемся к защищенным атрибутам напрямую
        return self._income['wage'] + self._income['bonus']


if __name__ == '__main__':
    p = Position('Илья', 'Тестов', 'Контролер', 50_000, 10_000)
    p2 = Position('Анна', 'Тишина', 'Директор', 85_000, 15_000)

    print(p.position)
    print(p.get_full_name())
    print(p.get_total_income(), end='\n\n')

    print(p2.position)
    print(p2.get_full_name())
    print(p2.get_total_income())
