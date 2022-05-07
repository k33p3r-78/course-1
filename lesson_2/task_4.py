from random import uniform, randint

price_list = []
for i in range(randint(10, 20)):
    price_list.append(uniform(1.0, 1000.99))

# price_list = [ 34, 23.29, 43, 23.23, 546.04 ]

print('Исходный список: \n', price_list)

tmp_arr = []
for price in price_list:
    rub = int(price)
    kop = int((price - rub) * 100)

    tmp_arr.append(f'{rub} руб. {kop:02} коп.')
print(', '.join(tmp_arr))

print('\n\nДоказательство операции in place:')
print(f'\tid перед сортировкой: {id(price_list)}')
price_list.sort()
print(f'\tid после сортировки: {id(price_list)}')
print(price_list, '\n')


new_price_list = list(reversed(price_list))
print(f'id оригинального списка: {id(price_list)}')
print(f'id нового списка: {id(new_price_list)}')
print(new_price_list)
print('5 самых дорогих товаров:')
for i in range(5):
    print(f'{new_price_list[i]:.2f}')