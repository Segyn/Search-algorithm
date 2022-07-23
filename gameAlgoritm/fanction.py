# Алгоритм пузырькового метода

# Создаем ввод числа пользователем
def start_algorithm():
    user_number = input('Введите число то 0 до 100: ')
    # проверяем что введено число
    if user_number.isnumeric():
        user_number = int(user_number)
        max_algorithm(user_number)
    else:
        print('Вы ввели не число')
        start_algorithm()


# Создаем максимальное число
def max_algorithm(user_number: int):
    max_number = 100
    if user_number > max_number:
        print(f'Вы вели число больше разрешённого {max_number}')
        start_algorithm()
    min_algorithm(user_number, max_number)


# Создаем минимальное число
def min_algorithm(user_number: int, max_number: int):
    min_number = 0
    if user_number < max_number:
        print(f'Вы вели число меньше разрешённого {min_number}')
        start_algorithm()
    search_algorithm(user_number, min_number, max_number)


# Алгоритм поиска
def search_algorithm(user_number: int, min_number: int, max_number: int):
    search = int((max_number - min_number) / 2)
    if min_number == user_number == min_number + search == user_number or max_number - search == user_number == max_number == user_number:
        return print('Конец')
    if min_number + search > user_number:
        max_number -= search
    else:
        min_number += search

    search_algorithm(user_number, min_number, max_number)


if __name__ == '__main__':
    start_algorithm()
