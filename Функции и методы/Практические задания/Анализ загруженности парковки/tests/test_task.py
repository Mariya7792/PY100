import inspect
import unittest

try:
    from task import calculate_parking_load
except ImportError:
    raise AssertionError(
        'Проверьте, что объявлена функция `calculate_parking_load`'
    )


class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        sign = inspect.signature(calculate_parking_load)
        assert len(sign.parameters) == 2, (
            'Убедитесь, что при объявлении функции `calculate_parking_load` '
            'указано два аргумента.'
        )

        first_arg, second_arg = sign.parameters.values()

        first_arg_expected_name = "total_parking_spaces"
        assert first_arg.name == first_arg_expected_name, (
            f'Убедитесь, что первый аргумент функции '
            f'`calculate_parking_load` называется `{first_arg_expected_name}`'
        )
        assert first_arg.default == inspect.Parameter.empty, (
            f'Убедитесь, что первый аргумент функции '
            f'`calculate_parking_load` является позиционным аргументом.'
        )

        second_arg_expected_name = "occupied_parking_spaces"
        assert second_arg.name == second_arg_expected_name, (
            f'Убедитесь, что второй аргумент функции '
            f'`calculate_parking_load` называется `{second_arg_expected_name}`'
        )
        assert second_arg.default == inspect.Parameter.empty, (
            f'Убедитесь, что второй аргумент функции '
            f'`calculate_parking_load` является позиционным аргументом.'
        )

    def test_calculate_parking_load(self):
        values = (
            (100, 60, 60,),
        )
        for total_parking_spaces, occupied_parking_spaces, expected_result in values:
            actual_result = calculate_parking_load(total_parking_spaces, occupied_parking_spaces)

            assert actual_result is not None, (
                "Проверьте, что в функции `calculate_parking_load` объявлен оператор, "
                "возвращающий значение из функции."
            )

            assert actual_result == expected_result, (
                "Проверьте, что в функции `calculate_parking_load` "
                "верно рассчитывается жилая плотность и применено округление значения."
            )
