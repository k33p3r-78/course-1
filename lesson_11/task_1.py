import datetime


class DateInitError(Exception): pass

class Date:


    def __init__(self, date_str):
        try:
            date_ints = Date.date_to_ints(date_str)
        except ValueError:
            raise DateInitError('Некорректный формат даты')
        if Date.validate(*date_ints):
            self._date = date_ints
        else:
            raise DateInitError('В дате присутствуют некорректные числа')

    @classmethod
    def date_to_ints(cls, date_str):
        day, month, year = date_str.split('-')
        return int(year), int(month), int(day)

    @staticmethod
    def validate(year, month, day):
        try:
            datetime.date(year, month, day)
        except ValueError:
            return False
        else:
            return True

    def __str__(self):
        return f'{self._date[0]}.{self._date[1]}.{self._date[2]}'


if __name__ == '__main__':
    lst_date = ["31-12-2021", "32-12-2022", "12-12--2022" ]

    for date in lst_date:
        try:
            print(Date(date))
        except DateInitError as err:
            print(f'Дата: {date},\tрезультат: {err}')








