import os
from pathlib import Path
import json


res_dict = {}
borders = [100, 1000, 10000, 100000]
borders.sort()

dir_to_scan = Path().resolve().joinpath('some_data')
dirs_list = [dir_to_scan]
for root, dirs, files in os.walk(dir_to_scan):
    dirs_list.append(root)
for border in borders:
    res_dict[border] = 0

for path in dirs_list:
    for file in os.scandir(path):
        for border in borders:
            if file.stat().st_size < border:
                res_dict[border] += 1
                break

print(json.dumps(res_dict, indent=4))
