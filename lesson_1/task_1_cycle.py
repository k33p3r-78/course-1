# 1. Реализовать вывод информации о промежутке времени в зависимости 
# от его продолжительности duration в секундах: до минуты: <s> сек;
# до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; 
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# Примеры:

# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек

day = 86400
hour = 3600
minute = 60

while True:
    duratation = int(input("Введите продолжительность в секундах: "))
    if not duratation: break

    days = duratation // day
    duratation %= day
    hours = duratation // hour
    duratation %= hour
    mins = duratation // minute
    duratation %= minute

    if days:
        print(days, 'дн', end=' ')
    if hours:
        print(hours, 'час', end=' ')
    if mins:
        print(mins, 'мин', end=' ')
    print(duratation, 'сек')