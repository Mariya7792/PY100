import inspect
import unittest

try:
    from task import is_palindrome
except ImportError:
    raise AssertionError(
        'Проверьте, что объявлена функция `is_palindrome`'
    )


class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        sign = inspect.signature(is_palindrome)
        assert len(sign.parameters) == 1, (
            'Убедитесь, что при объявлении функции `is_palindrome` '
            'указан один аргумент.'
        )

        first_arg, = sign.parameters.values()

        assert first_arg.default == inspect.Parameter.empty, (
            f'Убедитесь, что первый аргумент функции '
            f'`is_palindrome` является позиционным аргументом.'
        )

    def test_is_palindrome_true(self):
        values = [
            "Кит на море не романтик"
        ]
        for string in values:
            assert is_palindrome(string) is True, (
                f"Строка '{string}' является палиндромом. "
                f"Проверьте в функции `is_palindrome` логику проверки палиндрома. "
            )

    def test_is_palindrome_false(self):
        values = [
            "Прочая строка"
        ]
        for string in values:
            assert is_palindrome(string) is False, (
                f"Строка {string} является палиндромом. "
                f"Проверьте в функции `is_palindrome` логику проверки палиндрома. "
            )
