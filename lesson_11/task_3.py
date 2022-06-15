class NotDigitError(ValueError): pass
class StopInputError(KeyboardInterrupt): pass


def get_digit():
    digit = input('Введите целое число или нажмите Enter для выхода: ')
    if not digit: raise StopInputError
    if not digit.isdigit(): raise NotDigitError
    return int(digit)


if __name__ == '__main__':
    res = []
    while True:
        try:
            res.append(get_digit())
        except NotDigitError:
            print('Ввод не является числом, повторите ввод')
        except (StopInputError, KeyboardInterrupt):
            print(f'\nВы ввели: {res}')
            break


