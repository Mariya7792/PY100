# TODO решите задачу
def task() -> float:
    ...


print(task())
# def init_field(field:list, emply_cell: str = EMPTY_CELL) -> list:
#     """
#     Создает пустое поле для начала игры
#     :return: возвращает словарь
#     """
#     horizontal = int(input('Введите высоту поля: '))
#     vertical = int(input('Введите длину поля: '))
#     field = [horizontal, vertical]


#     return field

# def get_char_val(text: str, req_list: list) -> str:
#     """
#     Пользователь вводит символ. Проверяем, сответствует ли элемент, введенный пользователем, условиям задачи.
#     Если нет, то просим заново ввести.
#     :param text: Символ игрока
#     :param req_list: Знак, который можно ввести
#     :return: Знак, выбранный пользователем
#     """
#     req_list = ['0', '*']
#     while True:
#         text = input(f'Пожалуйста, введите знак из списка {req_list}:')
#         if text not in req_list:
#             print(f'Пожалуйста, введите только знак из списка {req_list}!')
#             continue

#         return text


# def get_index_from_table(field, size: int):
#     """
#     Спрашиваем у игрока, куда он хочет поставить символ. Получив ответ, проверяем, можно ли туда поставить
#     :param field:
#     :param size:
#     :return: Возвращаем индекс, куда можно поставить
#     """
#     field = init_field()

# def is_win(field):
#     """
#     Проверка, выигрышная ли компинация
#     :param field:
#     :return:
#     """

# def change_player(current_player: str)
