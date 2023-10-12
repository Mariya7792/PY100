def exists_student_by_lastname(students, lastname):
    ...  # TODO Напишите проверку студента с заданной фамилией


students_list = [
    {'имя': 'Иван', 'фамилия': 'Иванов'},
    {'имя': 'Петр', 'фамилия': 'Петров'},
    {'имя': 'Анна', 'фамилия': 'Иванова'},
    {'имя': 'Елена', 'фамилия': 'Сидорова'},
]

for find_lastname in ['Иванов', 'Пупкин']:
    is_exists_lastname = exists_student_by_lastname(students_list, find_lastname)
    print(f"Есть ли в базе студент с фамилией {find_lastname}? {is_exists_lastname}")
