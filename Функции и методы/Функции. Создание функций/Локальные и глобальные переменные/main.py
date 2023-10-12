PI = 3.1415  # Константное значение


def calculate_circumference(r):
    # r и circumference  - локальные переменные для функции calculate_circumference
    circumference = 2 * PI * r  # PI - глобальная переменная
    return circumference


def calculate_area(r):
    # r и area  - локальные переменные для функции calculate_area
    area = PI * r ** 2  # PI - глобальная переменная
    return area


radius = 5
print(f"Длина окружности с радиусом {radius}: {calculate_circumference(radius):.4f}")
print(f"Площадь круга с радиусом {radius}: {calculate_area(radius):.4f}")

