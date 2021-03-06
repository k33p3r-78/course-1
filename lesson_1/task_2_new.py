# Техническое задание:

# Для всех нечетных чисел диапазона [1, 1000]
# вычислить их куб
# вычислить сумму цифр куба
# если сумма цифр куба делится нацело на 7, то добавить в накопительную сумму исходное число.
# При решении задачи использовать только арифметические операции и цикл while.
# Не используем списки, функцию range, преобразование числа в строку/список.
# Ваш алгоритм должен корректно работать для всех чисел интервала от 1 до 1000,
# но и легко изменяться для другого диапазона чисел, например от 1 до 10000000.

res_sum = 0
i = 0
while i < 1000:
    i += 1
    if i % 2 == 1: 
        cube = i ** 3
        digits = cube
        digits_sum = 0
        while digits // 10:
            digits_sum += digits % 10
            digits //= 10
        digits_sum += digits
        if not digits_sum % 7: 
            res_sum += i
            print(f"{i}^3 = {cube}; [{digits_sum}] {res_sum}")

    