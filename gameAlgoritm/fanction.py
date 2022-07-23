def start_algorithm():
    user_number = int(input('Введите число то 0 до 100: '))
    max_number = 100
    min_number = 0
    search_algorithm(user_number, min_number, max_number)


def search_algorithm(user_number: int, min_number: int, max_number: int):
    search = int((max_number - min_number) / 2)
    print(search)
    if search == user_number:
        return print('Конец')
    if search < user_number:
        min_number = search
    if search > user_number:
        max_number = search
    print(min_number)
    print(max_number)
    search_algorithm(user_number, min_number, max_number)


if __name__ == '__main__':
    start_algorithm()
