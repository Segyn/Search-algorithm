# Алгоритм пузырькового метода поиска целого числа из сортированного набора чисел


# начальное число всегда равен нулю.
def min_algorithm():
    min_number = 0
    max_algorithm(min_number)


# Максимальное число из набора
def max_algorithm(min_number: int):
    # Получаем максимальное число
    max_number = input('Введите целое положительное максимальное число набора от нуля до ->')
    # Проверяем полученный набор
    if max_number.isdigit():
        max_number = int(max_number)
        if max_number == 0:
            return print('Поиск не требуется')
        start_algorithm(min_number, max_number)
    else:
        print('Неправильный ввод! Повторите ввод согласно запроса!\n')
        max_algorithm(min_number)


# Ввод искомого числа
def start_algorithm(min_number, max_number):
    user_number = input(f'Введите для поиска целое число то 0 до {max_number}: ->')
    # проверяем что ввод
    if user_number.isdigit():
        user_number = int(user_number)
        if user_number > max_number:
            print('Вы ввели число больше максимального! Повторите ввод согласно запроса!\n')
        search_algorithm(user_number, min_number, max_number)
    else:
        print('Неправильный ввод! Повторите ввод согласно запроса!\n')
        start_algorithm(min_number, max_number)


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
    min_algorithm()
