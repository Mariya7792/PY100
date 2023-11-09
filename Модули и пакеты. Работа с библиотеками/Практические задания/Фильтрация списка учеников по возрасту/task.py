# TODO Напишите функцию calculate_average_age
def calculate_average_age(list_):
    list_compressed = [age_['age'] for age_ in list_]
    average = sum(list_compressed) / len(list_compressed)
    return average


def filter_students_by_age(list_, average_age):
    list_compressed = [age_ for age_ in list_ if age_['age'] < average_age]
    return list_compressed


# TODO Напишите функцию filter_students_by_age


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
    print("Средний возраст учеников:", calculate_average_age(students_list))
    print(filter_students_by_age(students_list, calculate_average_age(students_list)))

    # Фильтрация учеников по возрасту
    # TODO Офильтруйте учеников
    # print("Список учеников с возрастом меньше среднего:")
    # for current_student in ...:
    #     print(current_student['name'])
