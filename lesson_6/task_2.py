# 2. [Задача со звездочкой]: усложненный вариант задания 1. 
# Найти IP адрес спамера и количество отправленных им запросов по данным файла логов 
# из предыдущего задания. Спамер — это клиент, отправивший больше всех запросов.
# Формат вывода результата:

# Вывести IP спамера и количество запросов от него.
# Техническое задание

# Код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# У нас изначально нет никакой информации о максимальном количестве запросов. Его надо определить из лог-файла.
# Не используйте сторонние модули для подсчетов, типа «count» - они вам не нужны.
# Не используйте затратные операций типа сортировки и поисков. Они здесь абсолютно избыточны. 
# Для примера представьте, что более половина лог-файла - это запросы от спамера. 
# Оцените эффективность вашего алгоритма в таком случае.

from pathlib import Path
import task_1


log_path = Path().resolve().joinpath("data", "task_1", "nginx_logs.txt")
connect_log = task_1.get_log_summary(log_path)
connect_count = {}
max_connect_ip = connect_log[0][0]
for ip, req, page in connect_log:
    if ip not in connect_count:
        connect_count[ip] = 1
    else:
        connect_count[ip] += 1
        if connect_count[ip] > connect_count[max_connect_ip]:
            max_connect_ip = ip

print(f"ip: {max_connect_ip}\nnumber of connections: {connect_count[max_connect_ip]}")









