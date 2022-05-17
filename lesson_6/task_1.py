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

from pathlib import Path


log_path = Path().resolve().joinpath("data", "task_1", "nginx_logs.txt")
nginx_logs_file = open(log_path, mode = "rt", encoding = "UTF-8")
res_list = []
for line in nginx_logs_file:
    ip_start = 0
    ip_end = line.find(" - - [")
    ip = line[ip_start:ip_end]
    req_format_start = line.find("] \"") + 3
    req_format_end = line.find(" /")
    req_format = line[req_format_start:req_format_end]
    target_start = req_format_end + 1
    target_end = line.find(" HTTP/1.1")
    target = line[target_start:target_end]
    
    res_list.append( (ip, req_format, target) )
nginx_logs_file.close()

print(*res_list, sep='\n')

