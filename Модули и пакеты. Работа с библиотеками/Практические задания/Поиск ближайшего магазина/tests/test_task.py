import ast
import unittest

try:
    from task import get_nearest_shop
except ImportError:
    raise AssertionError(
        'Не удаляйте функцию `get_nearest_shop`'
    )


def has_lambda(code):
    tree = ast.parse(code)

    for node in ast.walk(tree):
        if isinstance(node, ast.Lambda):
            return True

    return False


class TestCase(unittest.TestCase):
    def test_remove_function_get_distance(self):
        msg = "Функция `get_distance` должна быть удалена."
        with self.assertRaises(ImportError, msg=msg):
            from task import get_distance

    def test_get_nearest_shop(self):
        shop_points = [
            (4.5, 3),
            (2.1, -1),
            (6.8, -3),
            (1.4, 2.9)
        ]
        expected_value = (2.1, -1)
        actual_value = get_nearest_shop(shop_points)

        assert actual_value == expected_value, (
            'Проверьте, что функция `get_nearest_shop` верно находит координаты ближайшего магазина.'
        )

    def test_use_lambda_in_get_nearest_shop(self):
        filepath = "task.py"
        with open(filepath) as f:
            assert has_lambda(f.read()) is True, (
                'Проверьте, что в функции `get_nearest_shop` используется lambda функция.'
            )
