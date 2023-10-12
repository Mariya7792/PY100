def convert_to_uppercase(colors: list[str]) -> list[str]:
    """Функция для преобразования каждого цвета в верхний регистр."""
    return ...  # TODO Преобразовать цвета в верхний регистр


if __name__ == '__main__':
    colors_list = ['#ff0000', '#00ff00', '#0000ff']
    converted_colors = convert_to_uppercase(colors_list)
    print(converted_colors)  # ['#FF0000', '#00FF00', '#0000FF']
