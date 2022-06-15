# Техническое задание

# Данные файлов синхронизированы построчно: 1-ой строке файла с ФИО соответствует 1-ая строка файла с хобби и т.п.
# При хранении данных используется принцип: одна строка — один пользователь.
# Разделитель между значениями — запятая. Не используем пакеты для парсинга CSV файлов. 
# При формировании словаря - хобби следует разделить символом «точка с запятой».
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, то для оставшихся ФИО использовать вместо хобби None.
# Если наоборот — формируем словарь, исходя из количества ФИО и выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Вы можете использовать здесь функции zip и zip_longest, но лучше обойтись без них.
# Усложнение:
# Выполните запись результирующего словаря в файл json формата. Сделайте так чтобы русские букву читались как обычный текст, без преобразования в коды unicode.

from pathlib import Path
import json

users_path = Path().resolve().joinpath("data/task_3/task_3_users.csv")
hobby_path = Path().resolve().joinpath("data/task_3/task_3_hobby.csv")
result_path = Path().resolve().joinpath("data/task_3/task_3_rezult.txt")

res_dict = {}

with open(users_path, mode='rt', encoding="UTF-8") as users_file:
    with open(hobby_path, mode='rt', encoding="UTF-8") as hobby_file:
        for user_line in users_file:
            key = user_line.split(',')
            key = f"{key[0][0]}{key[1][0]}{key[2][0]}"

            hobby_line = hobby_file.readline().strip()
            hobby_line = ';'.join(hobby_line.split(','))
            if not hobby_line: hobby_line = None

            res_dict[key] = hobby_line
        if hobby_file.readline(): exit(1)


with open(result_path, mode='wt', encoding="UTF-8") as result_file:
    json.dump(res_dict, result_file, ensure_ascii=False)












