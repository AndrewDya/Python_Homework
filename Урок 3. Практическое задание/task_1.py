"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""

"""
1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

list_seasons = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето',
                'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
try:
    num_month1 = int(input("Введите месяц в виде целого числа: "))
    print(list_seasons[num_month1 - 1])
except IndexError:
    print("Нужно ввести число в диапазоне месяцев")
except ValueError:
    print("Нужно ввеcти число")

dictionary = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето',
              7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима'}
try:
    num_month2 = int(input("Введите месяц в виде целого числа: "))
    dictionary[num_month2]
    for key in dictionary:
        if key == num_month2:
            print(dictionary[num_month2])
except ValueError:
    print("Нужно введите число")
except KeyError:
    print("Нужно ввести число в диапазоне месяцев")
