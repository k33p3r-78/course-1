# 1. Распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# Техническое задание

# Не использовать библиотеки для парсинга. Только работа со строками.
# Создать список кортежей вида: '(<remote_addr>, <request_type>, <requested_resource>)'. Именно список кортежей.
# Код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# Вывести список на экран.
# Формат вывода результата:


# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'HEAD', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_1'),
#     ...
# ]

from pathlib import PurePath, Path


log_path = Path().joinpath("data", "task_1", "nginx_logs.txt")
print(log_path.resolve())
nginx_logs_file = open(log_path, mode = "rt", encoding = "UTF-8")
for line in nginx_logs_file:
    print(line)
    break
nginx_logs_file.close()