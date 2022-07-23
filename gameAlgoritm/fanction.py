# Алгоритм пузырькового метода поиска целого числа из сортированного набора чисел


# начальное число всегда равен нулю.
def min_algorithm():
    min_number = 0
    return max_algorithm(min_number)


# Максимальное число из набора
def max_algorithm(min_number: int):
    # Получаем максимальное число
    max_number = input('Введите целое положительное максимальное число набора от нуля до ->')
    # Проверяем полученный набор
    if max_number.isdigit():
        max_number = int(max_number)
        if max_number == 0:
            return print('Поиск не требуется')
        return start_algorithm(min_number, max_number)
    else:
        print('Неправильный ввод! Повторите ввод согласно запроса!\n')
        return max_algorithm(min_number)


# Ввод искомого числа
def start_algorithm(min_number, max_number):
    user_number = input(f'Введите для поиска целое число то 0 до {max_number}: ->')
    # проверяем ввод
    if user_number.isdigit():
        user_number = int(user_number)
        if user_number > max_number:
            print('Вы ввели число больше максимального! Повторите ввод согласно запроса!\n')
            return start_algorithm(min_number, max_number)
        if user_number == min_number or user_number == max_number:
            return print('Поиск завершён за одну попытку')
        return counter_algorithm(user_number, min_number, max_number, 0)
    else:
        print('Неправильный ввод! Повторите ввод согласно запроса!\n')
        return start_algorithm(min_number, max_number)


# Счетчик
def counter_algorithm(user_number: int, min_number: int, max_number: int, attempt_counter):
    attempt_counter += 1
    return search_algorithm(user_number, min_number, max_number, attempt_counter)


# Алгоритм поиска
def search_algorithm(user_number: int, min_number: int, max_number: int, attempt_counter):
    search = int((max_number - min_number) / 2)
    if min_number == user_number or min_number + search == user_number or max_number - search == user_number or max_number == user_number:
        return print(f'Поиск завершён за {attempt_counter} попыток')
    if min_number + search > user_number:
        max_number -= search
        attempt_counter += 1
    else:
        min_number += search
        attempt_counter += 1

    return search_algorithm(user_number, min_number, max_number, attempt_counter)


if __name__ == '__main__':
    min_algorithm()
