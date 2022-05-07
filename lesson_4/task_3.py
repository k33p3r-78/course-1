# [Задача со звездочкой]: усложненный вариант задания 2. Доработать функцию currency_rates: 
# теперь она должна возвращать курс валюты и дату, которая передаётся в ответе сервера.
# Название новой функции currency_rates_advanced.
# Условие задачи
# Техническое задание

# Все требования задания 2 остаются в силе.
# Функция должна вернуть список или кортеж, содержащий дату и курс валюты.
# Дата должна быть объектом date пакета datetime стандартной библиотеки. 
# Для ее создания используйте функции пакета datetime. Если это слишком сложно - оставьте дату строкой.
# Формат вывода результата:

# Вызовите функцию для нескольких валют, обязательно для несуществующей валюты, продемострируйте правильность работы.
# Примеры/Тесты:


# >>> url = "<http://www.cbr.ru/scripts/XML_daily.asp>"
# >>> currency_rates_advanced(url, "USd")
# ([datetime.date(2021, 10, 15)], 71.7846)
# >>> currency_rates_advanced(url, "EuR")
# ([datetime.date(2021, 10, 15)], 83.3347)
# >>> currency_rates_advanced(url, "GBP")
# ([datetime.date(2021, 10, 15)], 98.3449)
# >>> currency_rates_advanced(url, "GBP2")
# ([datetime.date(2021, 10, 15)], None)

from requests import get, utils
from datetime import date


def currency_rates_advanced(url, currency):
    """Функция возвращает текущий курс валюты по его буквенному названию"""

    # Загружаем данные по ссылке
    r = get(url)
    encodings = utils.get_encoding_from_headers(r.headers)
    content = r.content.decode(encoding=encodings)
    # Получаем дату и обрезаем служебную информацию
    day, month, year = map(int, content[61:70].split('.'))
    res_date = date(year, month, day)
    content = content[103:-10]
    # Генерируем словарь { название: курс к рублю }
    exchange_rate = {}
    for line in content.split("</Valute>"):
        if not line: continue
        char_code_from = line.find('<CharCode>') + len('<CharCode>')
        char_code_to = line.find('</CharCode>')
        value_from = line.find('<Value>') + len('<Value>')
        value_to = line.find('</Value>')
        char_code = line[char_code_from:char_code_to]
        value = line[value_from:value_to]
        exchange_rate[char_code] = float(value.replace(",", "."))

    # Если запрошеная валюта есть в словаре, возвращаем значение
    currency = currency.upper()
    if currency in exchange_rate:
        return res_date, exchange_rate[currency]
    else:        return None


if __name__ == '__main__':
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    print(currency_rates_advanced(url, "USd"))
    print(currency_rates_advanced(url, "EuR"))
    print(currency_rates_advanced(url, "GBP"))
    print(currency_rates_advanced(url, "GBP2"))

