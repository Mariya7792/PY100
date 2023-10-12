from collections import Counter

# Создание Counter из строки
c = Counter('abracadabra')
print(c)  # Вывод: Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# Получение наиболее часто встречающегося элемента
most_common = c.most_common(1)
print(most_common)  # Вывод: [('a', 5)]
