arr1 = ['в', '5', 'часов', '17', 'минут', 'температура',
        'воздуха', 'была', '+5', 'градусов']
arr2 = ['примерно в', '23', 'часа', '8', 'минут', '03', 
        'секунд', 'температура', 'воздуха', 'была', '-5',
        'градусов Цельсия', 'темп', 'воды', '+12', 'градусов', 'Цельсия']
arr3 = ['+9', 'примерно в', '23', 'часа', '8', 'минут', '03',
        '05', 'секунд', 'температура', 'воздуха', 'была', '5', 
        'градусов Цельсия', 'темп','воды','+2.0','градусов',
        'Цельсия' ,'-2', '11']



extnd = False
for index, el in enumerate(arr1):
    if extnd:
        extnd = False
        continue
    if el.startswith('+') or el.startswith('-'):
        el = el[1:]
    if el.isnumeric():
        arr1.insert(index, '"')
        arr1.insert(index + 2, '"')
        extnd = True

res_str = ''
q_opened = False
for el in arr1:
    if el == '"' and not q_opened:
        res_str += ' ' + el
        q_opened = True
    elif el == '"' and q_opened:
        res_str += el
        q_opened = False
    elif q_opened:
        res_str += el
    else:
        res_str += ' ' + el

res_str = res_str.lstrip()
print(res_str)


################################################################

extnd = False
for index, el in enumerate(arr2):
    if extnd:
        extnd = False
        continue
    if el.startswith('+') or el.startswith('-'):
        el = el[1:]
    if el.isnumeric():
        arr2.insert(index, '"')
        arr2.insert(index + 2, '"')
        extnd = True

res_str = ''
q_opened = False
for el in arr2:
    if el == '"' and not q_opened:
        res_str += ' ' + el
        q_opened = True
    elif el == '"' and q_opened:
        res_str += el
        q_opened = False
    elif q_opened:
        res_str += el
    else:
        res_str += ' ' + el

res_str = res_str.lstrip()
print(res_str)


extnd = False
for index, el in enumerate(arr3):
    if extnd:
        extnd = False
        continue
    if el.startswith('+') or el.startswith('-'):
        el = el[1:]
    if el.isnumeric():
        arr3.insert(index, '"')
        arr3.insert(index + 2, '"')
        extnd = True

res_str = ''
q_opened = False
for el in arr3:
    if el == '"' and not q_opened:
        res_str += ' ' + el
        q_opened = True
    elif el == '"' and q_opened:
        res_str += el
        q_opened = False
    elif q_opened:
        res_str += el
    else:
        res_str += ' ' + el

res_str = res_str.lstrip()
print(res_str)