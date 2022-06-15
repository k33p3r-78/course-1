from pathlib import Path
import argparse


bakery_path = Path().resolve().joinpath('data/task_4/bakery.csv')

parser = argparse.ArgumentParser(description='Изменяет указанную сумму продаж')
parser.add_argument('num', type=int, help='Номер записи для редактирования')
parser.add_argument('value', type=int, help='Новое значение суммы продаж')

args = parser.parse_args()

num = args.num - 1
value = str(args.value)

with open(bakery_path, mode='r+t', encoding='UTF-8') as bakery_file:
    i = 0
    line = bakery_file.readline()
    while i < num and line:
        line = bakery_file.readline()
        i += 1
        
    if i != num:
        print('Продажа с указанным номером не найдена')
        exit()
    # bakery_file.write(value)
    # Как перезаписать сумму с длинной больше чем у новой -- понятно
    # Но если в новой сумме больше символов, то нужно сдвигать весь остаток файла

