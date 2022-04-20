arr = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for el in arr:
    name = el.split()[-1].title()
    position = ' '.join(el.split()[:-1]).lower()
    print(f'Привет, {position} {name}!')