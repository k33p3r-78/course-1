from pathlib import Path
import argparse


bakery_path = Path().resolve().joinpath('data/task_4/bakery.csv')

parser = argparse.ArgumentParser(description='Выводит суммы продаж из базы')
parser.add_argument('--start', type=int, default=1, help='Начиная с какой продажи выводить')
parser.add_argument('--end', type=int, default=0, help='До какой продажи выводить')

args = parser.parse_args()

start_sale = args.start - 1
end_sale = args.end

with open(bakery_path, mode='rt', encoding='UTF-8') as bakery_file:
    for line_no, line in enumerate(bakery_file):
        if line_no < start_sale: continue
        if end_sale and line_no >= end_sale: break
        print(line, end='')



