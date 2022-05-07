# [Задача со звездочкой]: Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. 
# Используйте аргументы командной строки.
# Условие задачи
# Техническое задание

# Скрипт должен корректно обрабатывать только одну переданную ему валюту.
# Сделайте значимые сообщения пользователю о работе скрипта. Например при неправильно переданных параметрах или их количестве.
# Использовать аргументы командной строки. Функцию input не использовать.
# Скрипт могут запустить вообще без параметров, а могут с любым количеством параметров. Это надо учесть.
# Сделайте скриншот нескольких вызовов скрипта с разными аргументами.
# Примеры/Тесты:


# py task-4_5.py USD
#        USD: 71.7846
# py task-4_5.py FFF
#        FFF: Не найдена валюта     

import argparse, utils


parser = argparse.ArgumentParser(description='Отображает текущий курс валюты.')
parser.add_argument('cur', metavar='CUR', type=str, help='Буквенное обозначение валюты eg. EUR')
parser.add_argument('--adv', '-a', action='store_true', default=False,
                    help='Расширенный режим')

args = parser.parse_args()

url = "http://www.cbr.ru/scripts/XML_daily.asp"
date = None
if args.adv:
    cr_res = utils.currency_rates_advanced(url, args.cur)
    if cr_res: 
        date, cr_res = cr_res
else:
    cr_res = utils.currency_rates(url, args.cur)

if not cr_res:
    print(f'\t{args.cur.upper()}: Не найдена валюта')
elif date:
    print(f'\t{args.cur.upper()}({date}): {cr_res}')
else:
    print(f'\t{args.cur.upper()}: {cr_res}')





