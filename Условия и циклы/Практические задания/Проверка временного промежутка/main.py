hour = 19

if 6 <= hour <= 11:
    print("Утро")
elif 12 <= hour <= 17:
    print("День")
elif 18 <= hour <= 20:
    print("Вечер")
elif 21 <= hour <= 5:
    print("Ночь")
else:
    print("Недопустимое количество часов")
