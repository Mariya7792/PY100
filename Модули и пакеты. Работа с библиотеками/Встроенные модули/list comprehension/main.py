import random

# Пример 1: Умножение каждого элемента списка на 2
numbers = [1, 2, 3, 4, 5]
new_numbers = [num * 2 for num in numbers]
print(new_numbers)

# Пример 2: Фильтрация положительных чисел
numbers = [1, -2, 3, -4, 5]
positive_numbers = [num for num in numbers if num > 0]
print(positive_numbers)

# Пример 3: Генерация списка случайных чисел от 1 до 10
numbers = [1, -2, 3, -4, 5]
random_numbers = [random.randint(1, 10) for _ in range(10)]
print(random_numbers)
