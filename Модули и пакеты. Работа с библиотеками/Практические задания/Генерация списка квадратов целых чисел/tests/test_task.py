import ast
import unittest

try:
    from task import generate_squares
except ImportError:
    raise AssertionError(
        'Не удаляйте функцию `generate_squares`'
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
        with open(filepath, encoding="utf-8") as f:

            assert contains_list_comprehension(f.read()) is True, (
                'Проверьте, что в функции `generate_squares` используется list comprehension.'
            )

    def test_correct_value(self):
        expected_value = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        actual_value = generate_squares(10)

        assert actual_value == expected_value, (
            'Проверьте, что в функция `generate_squares` верно вычисляет квадраты целых чисел.'
        )
