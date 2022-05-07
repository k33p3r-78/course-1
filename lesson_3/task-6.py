# [Задача со звездочкой]: усложненный вариант задания 5.
# Условие задачи
# Техническое задание

# Добавьте в функцию еще один аргумент, разрешающий или запрещающий повторы слов в шутках: 
# каждое слово можно использовать только в одной шутке. Тогда этот параметр логично сделать типом boolean.
# Функция должна вернуть список строк-шуток сколько потребовали или сколько получилось из условия уникальности.
# Проверьте работу функции для разного количества шуток. Убедитесь в том, что каждое слово встречается только один раз.

from random import choice

def get_jokes(number_of_jokes, list1, list2, list3, allow_repeats=True):
    """Функция генерирует заданное количество шуток из переданных списков слов
    параметр allow_repeats отвечает за повторное использование слов
    """

    res_jokes = []
    if allow_repeats:
        # Если повторы разрешены, генерируем заданное кол-во шуток
        for i in range(number_of_jokes):
            res_jokes.append(f'{choice(list1)} {choice(list2)} {choice(list3)}')
        return res_jokes
    else:
        # Приводим списки к общей длинне по самому короткому
        lst1 = []
        lst2 = []
        lst3 = []
        for itm1, itm2, itm3 in zip(list1, list2, list3):
            lst1.append(itm1)
            lst2.append(itm2)
            lst3.append(itm3)

        # Если повторы запрещены, пытаемся сгенерировать заданое кол-во шуток
        # пока не иссякнет список неиспользованных слов
        i = 0
        while i < number_of_jokes and len(lst1):
            # Выбираем случайное слово и удаляем его из списка
            wrd1 = choice(lst1); lst1.remove(wrd1)
            wrd2 = choice(lst2); lst2.remove(wrd2)
            wrd3 = choice(lst3); lst3.remove(wrd3)
            res_jokes.append(f'{wrd1} {wrd2} {wrd3}')
        return res_jokes
        


if __name__ == '__main__':
    nouns = ["автомобиль", "лес", "огонь", "город", "дом", "test"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "test2"]

    print(*get_jokes(10, nouns, adverbs, adjectives, allow_repeats=False), sep='\n')
    print()
    print(*get_jokes(2, nouns, adverbs, adjectives), sep='\n')