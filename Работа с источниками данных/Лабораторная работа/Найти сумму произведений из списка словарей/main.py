
def draw_field(size):
    # size = int(input("Пожалуйста, введите размер поля:" ))
    field = init_field(size)
    return field

def get_int_val(border: list(int, int) = None) -> int:
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
    # req_list = ['0', 'X']
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
    index = field[place_line][place_column]

    while True:
        if index == EMPTY_CELL:
            return index
        elif index > size:
            print("Вы вышли за пределы поля!")
            continue
        else:
            print("Здесь уже есть символ. Пожалуйста, выберите другое место!")
            continue

        return index

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
    current_player = get_char_val()

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
        if len(list_vertical[i::border]) == border and set(list_vertical[i::border]) == {'X'} or set(list_vertical[i::border]) == {'0'}:
            return True
        else:
            return False   
    
    # Проверка по диагонали
    list_diagonal_left = []
    list_diagonal_right = []
    index_left = 0
    index_right = -1
    for index in range(len(list_)):
        list_diagonal_left.append(list_[index][index_left])
        list_diagonal_right.append(list_[index][index_right])
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

    # TODO Написать реализацию

    """
    В работе использовать функции написанные выше

    Возможный алгоритм работы функции:

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

    field_beginning = init_field(border_number)
    field_for_game = draw_field(field_beginning)
    
    max_attempts = int(input("Введите максимальное число попыток: "))
    attempts = 0
    while attempts < max_attempts:
        current_player = set_player_in_field(field_for_game)
        

        if is_win == True:
            
        else:
            change_player()
    if attempts == max_attempts:
        return 'Ничья!'

    def app():
    """
    Запуск приложения игры крестики-нолики
    :return:
    """

    """
    В работе использовать функции написанные выше
    
    Здесь можете спросить у пользователя на каком полу он хочет играть
    Кто будет ходить первым, может это будет X, а может 0
    С кем будет играть пользователь, с другим человеком или с компьютером. Если с человеком, то запустите ему игру,
        если выберет с компьютером, то напишите, что пока это в разработке.
    """
    print('Добро пожаловать в игру крестики-нолики!')
    game_partner_choice = input('С кем вы хотели бы играть? С другим человеком(1) или компьютером(2)?')
    if game_partner_choice = '1':
        print('Игра запускается')
    else:
        print('Игра с компьютером пока в разработке')
    border_number = get_int_val([3,6]) 
    
    req_list = ['0', 'X']
    
    text_for_player = f'Выберите, каким символом будете играть из значений {req_list}:'))
    player1 = get_char_value(text_for_player, req_list)
    if player1 == 'X':
        player2 == 'O':
    else:
        player2 == 'X'
    print(f'Первый игрок выбрал {player1}, второй игрок будет ходить {player2}')
    game()


if __name__ == "__main__":
    app()





















"""
Задание на проект крестики-нолики.

Создать консольное приложение крестики-нолики.

Необходимо реализовать функциональность игры двух людей, сначала играет первый человек, потом второй.
Реализация игры с компьютером по желанию и не является обязательным требованием.

Желательно если ваша реализация не будет привязана к полю 3x3, т.е. если я захочу сыграть на поле размером 4x4,
то мне максимум нужно будет только изменить размер поля, а код менять не нужно. Однако, если данная задача является
сложной на данном этапе, то можно зафиксировать размер поля.

Приложение должно быть разбито на функции, отвечающие за свою функциональность.

Необходимо провести описание функции, её входных переменных и провести аннотацию входных и выходных переменных.

Ниже приведен прототип приложения можно его использовать для заполнения или можно сделать свою структуру.

"""

from typing import Union, Optional

EMPTY_CELL = " "


def init_field(size: int, empty_cell: str = EMPTY_CELL) -> list[list]:
    """
    Создаёт и возвращет пустое поле для игры

    :param size: размер поля
    :param empty_cell: чем заполняется пустая ячейка
    :return: отображение пустого поля в виде листа листов

    """
    # TODO Можно выбрать своё представление поля, допустим строковое или одномерный список
    return [[empty_cell] * size for _ in range(size)]


def draw_field(field):
    """
    Функция рисует поле
    :param field: Объект поля
    :return: None
    """
    pass  # TODO Написать реализацию


def get_int_val(text: str, border: tuple[int, int] = None) -> int:
    """
    Проверяет и возвращает число (это может быть необходимо когда вы хотите проверить,
        что пользователь ввел именно число и это число лежит в диапазоне border[0] и border[1]).
        Спрашиваем у пользователя ввод числа с текстом text и проверяем что оно соответствует требованиям, если не
        соответствует хотя бы одному требованию, то заново просим ввести число.

    :param text: Текст перед получением числа
    :param border: Ограничение на число (минимум, максимум)
    :return: Возвращает число, которое ввёл пользователь и прошедшее все проверки
    """
    # TODO Написать реализацию

    return


def get_char_val(text: str, req_list: list) -> str:
    """
    Проверяет и возвращает строку из необходимого списка элеменов (req_list).
    Спрашиваем у пользователя ввод строку с текстом text и проверяем что оно соответствует требованиям, если не
        соответствует хотя бы одному требованию, то заново просим ввести строку.

    :param text: Текст перед получением числа
    :param req_list: Ограничение на число
    :return: Строка
    """
    # TODO Написать реализацию

    return


def get_index_from_table(field, size: int):
    """
    Получаем индексы куда можем поставить символ игрока.
    Спрашиваем у пользователя куда он хочет поставить, проверяем свободна ли ячейка, если занята,
        то просим заново выбрать куда поставить
    :param field:
    :param size:
    :return: Возвращаем индекс ячейки куда поставил пользователь
    """

    # TODO Написать реализацию

    return


def set_player_in_field(field,
                        current_player: str,
                        index_step):
    """
    Ставим игрока на поле. По переданным координатам index_step ставим игрока current_player на поле field
    :param field:
    :param current_player:

    :return: Возвращаем поле с текущим ходом игрока
    """

    # TODO Написать реализацию

    return


def is_win(field) -> bool:
    """
    Определяем произошла ли победа. Если на текущем поле выигрышная комбинация, то возвращает True. Если никто не выиграл,
        то возвращаем False
    :param field:
    :return: bool
    """

    # TODO Написать реализацию

    return


def change_player(current_player: str) -> str:
    """
    Определяет кто ходит следующий

    :param current_player: Текущий игрок
    :return:
    """

    # TODO Написать реализацию

    return


def game(player: str, size: int) -> Optional[str]:
    """
    Запускает игру

    :param player: игрок которых ходит первым
    :param size: размер поля
    :return: возвращаем None если ничья или возвращаем игрока кто победил
    """

    # TODO Написать реализацию

    """
    В работе использовать функции написанные выше
    
    Возможный алгоритм работы функции:
    
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


def app():
    """
    Запуск приложения игры крестики-нолики
    :return:
    """

    """
    В работе использовать функции написанные выше
    
    Здесь можете спросить у пользователя на каком полу он хочет играть
    Кто будет ходить первым, может это будет X, а может 0
    С кем будет играть пользователь, с другим человеком или с компьютером. Если с человеком, то запустите ему игру,
        если выберет с компьютером, то напишите, что пока это в разработке.
    """
     border_number = get_int_val([3,6]) 
    
    # TODO Написать реализацию


if __name__ == "__main__":
    app()
