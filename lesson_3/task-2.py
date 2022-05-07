# [Задача со звездочкой]: усложненный вариант задания 1. Написать функцию num_translate_adv, 
# которая корректно обработает числительные, начинающиеся с заглавной буквы. Если перевод сделать невозможно, вернуть объект None.
# Условие задачи
# Техническое задание

# Функция возвращает строку перевод. Или возвращает None, если перевести невозможно.
# Считаем, что только первая буква может быть заглавной.
# Обратите внимание, что функция возвращает перевод в том же регистре как и приняла.
# Выполнить вызов функции для нескольких слов и вывести на экран результаты.
# Примеры/Тесты:


# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

from winreg import KEY_CREATE_SUB_KEY


translete_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven':  'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(word):
    keys_cap = set()
    for key in translete_dict:
        keys_cap.add(key.capitalize())
        
    if word in translete_dict:
        return translete_dict[word]
    elif word in keys_cap:
        return translete_dict[word.lower()].capitalize()
    else:
        return None


if __name__ == '__main__':
    print(num_translate_adv(input('Введите числительное: ')))