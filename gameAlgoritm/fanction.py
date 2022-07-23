# Алгоритм пузырькового метода

def start_algorithm():
    user_number = int(input('Введите число то 0 до 100: '))
    max_number = 100
    min_number = 0
    search_algorithm(user_number, min_number, max_number)


def search_algorithm(user_number: int, min_number: int, max_number: int):
    search = int((max_number - min_number) / 2)
    if min_number == user_number or min_number + search == user_number or max_number - search == user_number or max_number == user_number:
        return print('Конец')
    if min_number + search > user_number:
        max_number -= search
    else:
        min_number += search

    search_algorithm(user_number, min_number, max_number)


if __name__ == '__main__':
    start_algorithm()
