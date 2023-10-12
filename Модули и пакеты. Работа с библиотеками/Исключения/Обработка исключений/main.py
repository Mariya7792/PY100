try:
    x = ...  # TODO Напишите input, чтобы запросить число
    result = 10 / x
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")
except ValueError:
    print("Ошибка: Введено некорректное число!")
else:
    print("Результат: ", result)
finally:
    print("Конец программы")
