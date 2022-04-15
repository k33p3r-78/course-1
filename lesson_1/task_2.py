# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. 
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. 
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

arr = []

for i in range(1000):
    if i % 2:
        arr.append(i ** 3)

odd_arr = []
for index, el in enumerate(arr):
    digits = 0
    while el // 10:
        digits += el % 10
        el //= 10
    else:
        digits += el % 10

    if not digits % 7:
        odd_arr.append(arr[index])

sum_arr = 0
for el in odd_arr:
    sum_arr += el

print(sum_arr)

############################################################################################################

for index, el in enumerate(arr):
    arr[index] = el + 17

sum_arr = 0
for index, el in enumerate(arr):
    digits = 0
    while el // 10:
        digits += el % 10
        el //= 10
    else:
        digits += el % 10

    if not digits % 7:
        sum_arr += arr[index]

print(sum_arr)
