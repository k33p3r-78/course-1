import argparse
from pathlib import Path


bakery_path = Path().resolve().joinpath('data/task_4/bakery.csv')

parser = argparse.ArgumentParser(description='Записывает сумму продаж в базу.')
parser.add_argument('sum', help='Сумма продаж')

args = parser.parse_args()

with open(bakery_path, mode='at', encoding='UTF-8') as bakery_file:
    bakery_file.write(args.sum + '\n')

