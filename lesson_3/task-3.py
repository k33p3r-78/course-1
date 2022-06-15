# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, 
# в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Условие задачи
# Техническое задание

# Количество передаваемых имен в функцию может быть любым. Считаем, что переданы будут только корректные строки. 
# Обратите внимание, что функция принимает произвольное количество параметров.
# Вернуть словарь с ключами, отсортированными в алфавитном порядке.
# Выполнить вызов функции для списка имен и вывести на экран словарь.
# Вы можете вывести на экран «красиво» - как в примере на каждой строке одна буква и список, но это не обязательно.
# Примеры/Тесты:


# >>> thesaurus("Иван", "Мария", "Петр", "Илья", "Артем", "Вадим", "Анатолий")
# {
#     "А": ["Артем", "Анатолий"],
#     "В": ["Вадим"],
#     "И": ["Иван", "Илья"], 
#     "М": ["Мария"],
#     "П": ["Петр"]
# }


def thesaurus(*names):
    res = {}
    for el in sorted(names):
        if el[0] in res:
            res[el[0]].append(el)
        else:
            res[el[0]] = [ el, ]
    
    for key, value in res.items():
        print(f'"{key}": {value}')


if __name__ == '__main__':
    thesaurus("Иван", "Мария", "Петр", "Илья", "Артем", "Вадим", "Анатолий")