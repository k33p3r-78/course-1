class MyZeroDivisionError(ZeroDivisionError):

    def __init__(self, a, b):
        self.a = a
        self.b = b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise MyZeroDivisionError(a, b)


if __name__ == '__main__':
    try:
        print(div(2, 1))
        print(div(6, 8))
        print(div(12, 0))
    except MyZeroDivisionError as err:
        print(f'Ошибка в выражении: {err.a} / {err.b}; Попытка деления на ноль')

