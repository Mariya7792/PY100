from typing import Union, Optional

EMPTY_CELL = "_"

def init_field(size:int, empty_cell: str = EMPTY_CELL) -> list:
    """
    Создает пустое поле для начала игры
    :return: возвращает словарь
    """
    return [[empty_cell] * size for _ in range(size)]


def draw_field(size):
    field = init_field(size)
    return field


def get_int_val(text: str, border: tuple[int, int] = None) -> int:
    while True:
        number = int(input(text))

        if number not in range(border[0], border[-1] + 1):
            print(f'Пожалуйста, введите число только в диапазоне от {border[0]} до {border[-1]}:')
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
            print(f'Пожалуйста, введите знак из списка {req_list}!')
            continue

        return symbol


def get_index_from_table(field, size: int):
    """
    Спрашиваем у игрока, куда он хочет поставить символ. Получив ответ, проверяем, можно ли туда поставить
    :param field:
    :param size:
    :return: Возвращаем индекс, куда можно поставить
    """
    while True:
        place_line = int(input("Укажите, в какую строку хотите поставить символ:")) - 1
        place_column = int(input("Укажите, в какой столбец хотите поставить символ:")) - 1
        index = [place_line, place_column]
        if field[place_line][place_column] == EMPTY_CELL:
            return index
        elif place_line > size or place_column > size:
            print("Вы вышли за пределы поля!")
            continue
        elif place_line == -1 or place_column == -1:
            print('Пожалуйста, введите символ!')
            continue
        else:
            print("Здесь уже есть символ. Пожалуйста, выберите другое место!")
            continue
            
            
def set_player_in_field(field,
                        current_player: str,
                        index_step):
    """
    Ставим игрока на поле. По переданным координатам index_step ставим игрока current_player на поле field
    :param field:
    :param current_player:

    :return: Возвращаем поле с текущим ходом игрока
    """
    index_lists = index_step[0]
    index_field = index_step[1]
    if field[index_lists][index_field] == EMPTY_CELL:
        field[index_lists][index_field] = current_player

    return field


def is_win(field):
    """
    Проверка, выигрышная ли компинация
    :param field:
    :return:
    """
    # Проверка по горизонтали
    for lists in field:
        if (set(lists)) == {'X'} or (set(lists)) == {'0'}:
            return True
    # Проверка по вертикали
    list_vertical = []
    for index in range(len(field)):
        for indexes in range(len(field)):
            list_vertical.append(field[index][indexes])
    border = len(field)
    for i in range(len(list_vertical)):
        if len(list_vertical[i::border]) == border and set(list_vertical[i::border]) == {'X'} or set(
                list_vertical[i::border]) == {'0'}:
            return True

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
    if set(list_diagonal_left) == {'X'} or set(list_diagonal_right) == {'X'}:
        return True
    elif set(list_diagonal_left) == {'0'} or set(list_diagonal_right) == {'0'}:
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
        next_player = '0'
    if current_player == '0':
        next_player = 'X'

    return next_player


def game(player: str, size: int) -> Optional[str]:
    """
    Запускает игру

    :param player: игрок которых ходит первым
    :param size: размер поля
    :return: возвращаем None если ничья или возвращаем игрока кто победил
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
            print(f'Поздравляем! Игрок, выбравший {player}, выиграл!')
            break
        else:
            attempts += 1
            print('Смена игрока')
            print('Ваше поле после хода последнего игрока:')
            player = change_player(player)
            for field in current_field:
                print(field)
            continue
    if attempts == max_attempts:
        print('Ничья!')


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
    border = [3, 6]
    text_for_border = f'Выберите размер поля. Пожалуйста, введите число в диапазоне от {border[0]} до {border[-1]}:'
    border_number = get_int_val(text_for_border, border)

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
