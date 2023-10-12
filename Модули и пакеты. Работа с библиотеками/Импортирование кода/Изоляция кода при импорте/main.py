from logic import calculate_square_area


if __name__ == '__main__':
    side_length = 5
    area = calculate_square_area(side_length)
    print(f"Функция `calculate_square_area` вызвана в модуле {__name__}")  # Печать переменной с названием модуля
    print(f"Площадь квадрата со стороной {side_length} равна {area}")
