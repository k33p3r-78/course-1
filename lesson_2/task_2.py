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
    signed = False
    if el.startswith('+') or el.startswith('-'):
        signed = el[:1]
        el = el[1:]
    if el.isnumeric():
        new_arr.extend(['"', arr1[index], '"'])
        continue
    
    if signed:
        new_arr.append(signed + el)
    else:
        new_arr.append(el)

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
    signed = False
    if el.startswith('+') or el.startswith('-'):
        signed = el[:1]
        el = el[1:]
    if el.isnumeric():
        new_arr.extend(['"', arr2[index], '"'])
        continue

    if signed:
        new_arr.append(signed + el)
    else:
        new_arr.append(el)

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
    signed = False
    if el.startswith('+') or el.startswith('-'):
        signed = el[:1]
        el = el[1:]
    if el.isnumeric():
        new_arr.extend(['"', arr3[index], '"'])
        continue

    if signed:
        new_arr.append(signed + el)
    else:
        new_arr.append(el)

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

