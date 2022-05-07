# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...) 
# и возвращающую курс этой валюты по отношению к рублю.
# Условие задачи
# Техническое задание

# Использовать библиотеку requests. В качестве API использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# В каком формате возвращен ответ? И какова его текстовая структура? Как из ответа излечь нужные данные?
# Функция currency_rates принимает два аргумента: строка с URL, куда стучимся и строку с кодом валюты (только одной). 
# Возвращает результат числового типа, например float. Если в качестве аргумента передали код валюты, которого нет в ответе, 
# вернуть объект None.
# Для извлечения данных использовать только методы объект str.
# Сделать работу функции не зависящей от того, в каком регистре был передан код валюты.
# Функция должна корректно обрабатывать любой код валюты. Правильность параметра url можно не проверять.
# Вводить коды валют с клавиатуры (input) необязательно.
# Формат вывода результата:

# Вызовите функцию для нескольких валют, обязательно для несуществующей валюты, продемострируйте правильность работы.
# Примеры/Тесты:


# >>> url = "<http://www.cbr.ru/scripts/XML_daily.asp>"
# >>> currency_rates(url, "USd")
# 71.7846
# >>> currency_rates(url, "EuR")
# 83.3347
# >>> currency_rates(url, "GBP")
# 98.3449
# >>> currency_rates(url, "GBP2")
# >>>

from requests import get, utils


def currency_rates(url, currency):
    """Функция возвращает текущий курс валюты по его буквенному названию"""

    # Загружаем данные по ссылке
    r = get(url)
    encodings = utils.get_encoding_from_headers(r.headers)
    content = r.content.decode(encoding=encodings)
    # Обрезаем служебную информацию
    content = content[103:-10]
    # Генерируем словарь название: курс к рублю
    exchange_rate = {}
    for line in content.split("</Valute>"):
        if not line: continue
        char_code_from = line.find('<CharCode>') + len('<CharCode>')
        char_code_to = line.find('</CharCode>')
        value_from = line.find('<Value>') + len('<Value>')
        value_to = line.find('</Value>')
        char_code = line[char_code_from:char_code_to]
        value = line[value_from:value_to]
        exchange_rate[char_code] = value

    # Если запрошеная валюта есть в словаре, возвращаем значение
    currency = currency.upper()
    if currency in exchange_rate:
        return exchange_rate[currency]
    else:
        return None


if __name__ == '__main__':
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    print(currency_rates(url, "USd"))
    print(currency_rates(url, "EuR"))
    print(currency_rates(url, "GBP"))
    print(currency_rates(url, "GBP2"))