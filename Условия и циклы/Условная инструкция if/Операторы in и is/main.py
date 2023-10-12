list_ = [1, 2, 3, 4, 5]

print("В списке есть число 7?", 7 in list_)  # False
print("В списке нет числа 7?", 7 not in list_)  # True

value = None

# Правильное сравнение с использованием `is`
if value is None:
    print("Переменная `value` равна None")
