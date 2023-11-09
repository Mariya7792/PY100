# TODO Напишите функцию get_student_names
def get_students_names(list_):
    list2 = [diction['name'] for diction in list_]
    return list2


if __name__ == '__main__':
    # Пример списка учеников
    students_list = [
        {
            "name": "Саша",
            "age": 27,
        },
        {
            "name": "Кирилл",
            "age": 52,
        },
        {
            "name": "Маша",
            "age": 14,
        },
        {
            "name": "Петя",
            "age": 36,
        },
        {
            "name": "Оля",
            "age": 43,
        },
    ]
    print(get_students_names(students_list))
