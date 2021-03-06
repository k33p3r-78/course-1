# Задан список чисел. Определить элементы списка, не имеющие повторений. 
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке
# Техническое задание

# Здесь нет условия создавать итератор/генератор или comprehensions.
# Сохранение исходного порядка в результирующем списке обязательно.
# Не используйте Counter из модуля collections или аналогичные.
# Примеры/Тесты:


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]

result = []
for el in src:
    if src.count(el) == 1:
        result.append(el)

print(result)
