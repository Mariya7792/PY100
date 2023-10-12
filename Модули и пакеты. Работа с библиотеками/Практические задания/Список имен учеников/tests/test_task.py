import ast
import unittest

try:
    from task import get_student_names
except ImportError:
    raise AssertionError(
        'Напишите функцию `get_student_names`'
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
                'Проверьте, что в функции `get_student_names` используется list comprehension.'
            )

    def test_correct_value(self):
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
        expected_value = ['Саша', 'Кирилл', 'Маша', 'Петя', 'Оля']
        actual_value = get_student_names(students)

        assert actual_value == expected_value, (
            'Проверьте, что в функция `get_student_names` возвращает имена из списка словарей по ключу `name`'
        )
