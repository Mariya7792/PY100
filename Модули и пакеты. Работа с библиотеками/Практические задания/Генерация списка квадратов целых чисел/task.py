def generate_squares(n):
    """
    Функция для генерации списка квадратов целых чисел от 0 до N.
    """
    # TODO заменить на list comprehension
    squares = []
    for i in range(n+1):
        squares.append(i**2)
    return squares


if __name__ == '__main__':
    # Проверка работы функции
    print(generate_squares(5))  # [0, 1, 4, 9, 16, 25]
    print(generate_squares(10))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print(generate_squares(0))  # [0]
