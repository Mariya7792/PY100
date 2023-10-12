import ast
import unittest

try:
    from task import generate_even_squares
except ImportError:
    raise AssertionError(
        'Не удаляйте функцию `generate_even_squares`'
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
                'Проверьте, что в функции `generate_even_squares` используется list comprehension.'
            )

    def test_correct_value(self):
        expected_value = [0, 4, 16, 36, 64, 100]
        actual_value = generate_even_squares(10)

        assert actual_value == expected_value, (
            'Проверьте, что в функция `generate_even_squares` верно вычисляет квадраты целых чисел.'
        )
