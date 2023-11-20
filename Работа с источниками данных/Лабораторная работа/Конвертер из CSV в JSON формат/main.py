from typing import Union, Optional

EMPTY_CELL = "_"

def init_field(size:int, empty_cell: str = EMPTY_CELL) -> list:
    """
    Создает пустое поле для начала игры
    :return: возвращает словарь
    """
    return [[empty_cell] * size for _ in range(size)]


def draw_field(size):
    # size = int(input("Пожалуйста, введите размер поля:" ))
    field = init_field(size)
    return field


def get_int_val(border: list = None) -> int:
    text = f'Пожалуйста, введите число в диапазоне от {border[0]} до {border[-1]}:'
    while True:
        number = int(input(text))

        if number not in range(border[0], border[-1] + 1):
            continue

        return number


def get_char_val(text: str, req_list: list) -> str:
    """
    Пользователь вводит символ. Проверяем, сответствует ли элемент, введенный пользователем, условиям задачи.
    Если нет, то просим заново ввести.
    :param text: Символ игрока
    :param req_list: Знак, который можно ввести
    :return: Знак, выбранный пользователем
    """
    while True:
        symbol = input(text)
        if symbol not in req_list:
            print(f'Пожалуйста, введите только знак из списка {req_list}!')
            continue

        return symbol

def get_index_from_table(field, size: int):
    """
    Спрашиваем у игрока, куда он хочет поставить символ. Получив ответ, проверяем, можно ли туда поставить
    :param field:
    :param size:
    :return: Возвращаем индекс, куда можно поставить
    """
    # field = init_field()
    # symbol = get_char_val()
    place_line = int(input("Укажите, в какую строку хотите поставить символ:")) - 1
    place_column = int(input("Укажите, в какой столбец хотите поставить символ:")) - 1

    place_in_field = field[place_line][place_column]
    for i in

    while True:
        if place_in_field == EMPTY_CELL:
            return index
        elif index > size:
            print("Вы вышли за пределы поля!")
            continue
        else:
            print("Здесь уже есть символ. Пожалуйста, выберите другое место!")
            continue

    # while True:
    # if field[place_line][place_column] == EMPTY_CELL:
    #     field[place_line][place_column] = symbol
    #
    #     return field

def set_player_in_field(field,
                        current_player: str,
                        index_step):
    """
    Ставим игрока на поле. По переданным координатам index_step ставим игрока current_player на поле field
    :param field:
    :param current_player:

    :return: Возвращаем поле с текущим ходом игрока
    """
    if field[index_step] == EMPTY_CELL:
        field[index_step] = current_player

    return field


def is_win(field):
    """
    Проверка, выигрышная ли компинация
    :param field:
    :return:
    """
    border = get_int_val()
    # Проверка по горизонтали
    for lists in field:
        if (set(lists)) == {'X'} or (set(lists)) == {'0'}:
            return True
        else:
            return False

    # Проверка по вертикали
    list_vertical = []
    for index in range(len(field)):
        for indexes in range(len(field)):
            list_vertical.append(field[index][indexes])
    for i in range(len(list_vertical)):
        if len(list_vertical[i::border]) == border and set(list_vertical[i::border]) == {'X'} or set(
                list_vertical[i::border]) == {'0'}:
            return True
        else:
            return False

            # Проверка по диагонали
    list_diagonal_left = []
    list_diagonal_right = []
    index_left = 0
    index_right = -1
    for index in range(len(field)):
        list_diagonal_left.append(field[index][index_left])
        list_diagonal_right.append(field[index][index_right])
        index_left += 1
        index_right -= 1
    if set(list_diagonal_left) or set(list_diagonal_right) == {'X'}:
        return True
    elif set(list_diagonal_left) or set(list_diagonal_right) == {'0'}:
        return True
    else:
        return False


def change_player(current_player: str) -> str:
    """
    Определяет кто ходит следующий

    :param current_player: Текущий игрок
    :return:
    """
    if current_player == 'X':
        return 'Ходит игрок, выбравший "0":'
    if current_player == '0':
        return 'Ходит игрок, выбравший "X":'

def game(player: str, size: int) -> Optional[str]:
    """
    Запускает игру

    :param player: игрок которых ходит первым
    :param size: размер поля
    :return: возвращаем None если ничья или возвращаем игрока кто победил
    """
    """
    Инициализируем поле для игры с заданным размером
    Отрисовываем текущее поле
    Инициализируем счетчик ходов
    Запускаем цикл while с условием пока счетчик меньше числа возможных ходов
        Получаем индексы куда поставил игрок (с проверками)
        Обновляем поле по тем индексам
        Отрисовываем поле
        Увеличиваем счётчик ходов
        Проводим проверку кто выиграл, если кто-то выиграл то возвращаем кто выиграл
        Меняем игрока на следующего
    Если шаги закончились, а никто не выиграл, значит у нас ничья!
    """

    field_beginning = init_field(size)
    field_for_game = draw_field(size)

    print('Ваше поле для игры:')
    for field in field_for_game:
        print(field)

    max_attempts = int(input("Введите максимальное число попыток: "))
    attempts = 0

    while attempts < max_attempts:
        player_chosen_index = get_index_from_table(field_for_game, size)
        current_field = set_player_in_field(field_for_game, player, player_chosen_index)
        if is_win(current_field) == True:
            return f'Вы выиграли!'
        else:
            attempts += 1
            change_player(player)
            print('Ваше поле после хода последнего игрока:')
            for field in current_field:
                print(field)


    if attempts == max_attempts:
        return 'Ничья!'


def app():
    """
    Запуск приложения игры крестики-нолики
    :return:
    """
    print('Добро пожаловать в игру крестики-нолики!')

    game_partner_choice = input('С кем вы хотели бы играть? С другим человеком(1) или компьютером(2)?')

    if game_partner_choice == '1':
        print('Игра запускается')
    else:
        print('Игра с компьютером пока в разработке. Запускаем игру с другим человеком')

    border_number = get_int_val([3, 6])

    req_list = ['0', 'X']

    text_for_player = f'Выберите, каким символом будете играть из значений {req_list}:'

    player_1 = get_char_val(text_for_player, req_list)
    if player_1 == 'X':
        player_2 = '0'
    else:
        player_2 = 'X'

    print(f'Первый игрок выбрал {player_1}, второй игрок: {player_2}')
    print('Начнем игру!')
    game(player_1, border_number)

if __name__ == "__main__":
    app()

