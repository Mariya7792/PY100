import ast
import unittest

try:
    from task import calculate_average_age, filter_students_by_age
except ImportError:
    raise AssertionError(
        'Напишите функцию `calculate_average_age` и `filter_students_by_age`'
    )


def contains_list_comprehension(code):
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.ListComp):
            return True
    return False


class TestCase(unittest.TestCase):
    def test_contains_list_comprehension(self):
        filepath = "task.py"
        with open(filepath) as f:
            assert contains_list_comprehension(f.read()) is True, (
                'Проверьте, что в функциях `calculate_average_age` и `filter_students_by_age`'
                ' используется list comprehension.'
            )

    def test_calculate_average_age(self):
        students = [
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
        expected_value = 34.4
        actual_value = calculate_average_age(students)

        assert actual_value == expected_value, (
            'Проверьте, что в функция `calculate_average_age` верно вычисляет средний возраст.'
        )

    def test_filter_students_by_age(self):
        students = [
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
        expected_value = [
            {
                "name": "Саша",
                "age": 27,
            },
            {
                "name": "Маша",
                "age": 14,
            },
        ]
        actual_value = filter_students_by_age(students, calculate_average_age(students))

        assert actual_value == expected_value, (
            'Проверьте, что в функция `filter_students_by_age` верно фильтрует учеников.'
        )
