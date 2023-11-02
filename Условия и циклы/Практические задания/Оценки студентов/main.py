# Список словарей со студентами и их оценками
students = [
    {"name": "Маша", "grade": 4},
    {"name": "Петя", "grade": 3},
    {"name": "Саша", "grade": 5},
    {"name": "Кирилл", "grade": 2},
    {"name": "Оля", "grade": 4},
]
for student in students:
    if student['grade'] > 3:
        print(student['name'] + '.', 'Оценка:', student['grade'])

# TODO Распечатать имена студентов с оценками выше тройки
