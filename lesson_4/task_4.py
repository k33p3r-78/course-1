# Написать свой модуль utils и перенести в него функцию currency_rates и currency_rates_advanced, 
# если вы решали задание 2. Создать скрипт, импортировать в него модуль utils и выполнить несколько 
# вызовов функции currency_rates. Убедиться, что ничего лишнего не происходит.
# Условие задачи
# Техническое задание

# В модуле utils не должно быть ничего лишнего, только объявление функций. 
# Если вы считает нужным поместить туда дополнительную инфу, например тесты - используйте конструкцию main.
# Основная программа импортирует модуль или только требуемые функции модуля, например currency_rates и currency_rates_advanced.
# После импорта выполните вызов функций в основной программе, аналогичный заданию 1 (и 2), чтобы убедиться, что все импортировалось верно.
# Примечание:

# Обратите внимание, что название создаваемого модуля совпадает с названием импортируемого из requests. Это не вызовет конфликтов.

import utils

url = "http://www.cbr.ru/scripts/XML_daily.asp"
print('currency_rates: ')
print(utils.currency_rates(url, "USd"))
print(utils.currency_rates(url, "EuR"))
print(utils.currency_rates(url, "GBP"))
print(utils.currency_rates(url, "GBP2"))
print('currency_rates_advanced: ')
print(utils.currency_rates_advanced(url, "USd"))
print(utils.currency_rates_advanced(url, "EuR"))
print(utils.currency_rates_advanced(url, "GBP"))
print(utils.currency_rates_advanced(url, "GBP2"))

