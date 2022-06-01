import os
from pathlib import Path
import json


res_dict = {}
borders = [100, 1000, 10000, 100000]
borders.sort()

dir_to_scan = Path().resolve().joinpath('some_data_adv')
dirs_list = [dir_to_scan]
for root, dirs, files in os.walk(dir_to_scan):
    dirs_list.append(root)
for border in borders:
    res_dict[border] = [0, []]

for path in dirs_list:
    for file in os.scandir(path):
        for border in borders:
            if file.stat().st_size < border:
                res_dict[border][0] += 1
                ext = file.name.split('.')[-1]
                if ext not in res_dict[border][1]:
                    res_dict[border][1].append(ext)
                break

res_name = dir_to_scan.name + '_summary.json'
try:
    with open(res_name, mode='wt', encoding='UTF-8') as f:
        f.write(json.dumps(res_dict, indent=2))
except OSError as e:
    print(e)


