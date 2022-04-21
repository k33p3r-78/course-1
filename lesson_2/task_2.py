arr1 = ['в', '5', 'часов', '17', 'минут', 'температура',
        'воздуха', 'была', '+5', 'градусов']
arr2 = ['примерно в', '23', 'часа', '8', 'минут', '03', 
        'секунд', 'температура', 'воздуха', 'была', '-5',
        'градусов Цельсия', 'темп', 'воды', '+12', 'градусов', 'Цельсия']
arr3 = ['+9', 'примерно в', '23', 'часа', '8', 'минут', '03',
        '05', 'секунд', 'температура', 'воздуха', 'была', '5', 
        'градусов Цельсия', 'темп','воды','+2.0','градусов',
        'Цельсия' ,'-2', '11']



new_arr = []
for index, el in enumerate(arr1):
    length = 2
    if el.startswith('+') or el.startswith('-'):
        el = el[1:]
        length = 3
    if el.isnumeric():
        new_arr.extend(['"', arr1[index].zfill(length), '"'])
        continue
    new_arr.append(arr1[index])

res_str = ''
q_opened = False
for el in new_arr:
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


#########################################################################


new_arr = []
for index, el in enumerate(arr2):
    length = 2
    if el.startswith('+') or el.startswith('-'):
        el = el[1:]
        length = 3
    if el.isnumeric():
        new_arr.extend(['"', arr2[index].zfill(length), '"'])
        continue
    new_arr.append(arr2[index])

res_str = ''
q_opened = False
for el in new_arr:
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


new_arr = []
for index, el in enumerate(arr3):
    length = 2
    if el.startswith('+') or el.startswith('-'):
        el = el[1:]
        length = 3
    if el.isnumeric():
        new_arr.extend(['"', arr3[index].zfill(length), '"'])
        continue
    new_arr.append(arr3[index])

res_str = ''
q_opened = False
for el in new_arr:
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

