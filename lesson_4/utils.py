from requests import get, utils
from datetime import date


def currency_rates(url, currency):
    """Функция возвращает текущий курс валюты по его буквенному названию"""

    # Загружаем данные по ссылке
    r = get(url)
    encodings = utils.get_encoding_from_headers(r.headers)
    content = r.content.decode(encoding=encodings)
    # Обрезаем служебную информацию
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
        return exchange_rate[currency]
    else:
        return None


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
    else:
        return None