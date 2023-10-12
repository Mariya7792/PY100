list_digit = [4, 9, 5, 1, 8, 4]  # TODO сформировать список цифр
print(list_digit)

sum_digit = sum(list_digit)
len_digit = len(list_digit)
min_digit = min(list_digit)
max_digit = max(list_digit)

print("Сумма цифр", sum_digit) # TODO сумма цифр
print("Количество цифр", len_digit)   # TODO количество цифр
print("Минимальная цифра", min_digit)  # TODO минимальная цифра
print("Максимальная цифра", max_digit)  # TODO максимальная цифра
print("Среднее арифметическое цифр", round(sum_digit / len_digit, 2))
