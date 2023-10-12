month = 15

# Создание списков с месяцами для каждого сезона
spring_months = [3, 4, 5]
summer_months = [6, 7, 8]
autumn_months = [9, 10, 11]
winter_months = [12, 1, 2]

# Проверка значения переменной month для определения сезона
if month in spring_months:
    print("Весна")  # Если month находится в списке весенних месяцев, выводим "Весна"
elif month in summer_months:
    print("Лето")  # Если month находится в списке летних месяцев, выводим "Лето"
elif month in autumn_months:
    print("Осень")  # Если month находится в списке осенних месяцев, выводим "Осень"
elif month in winter_months:
    print("Зима")  # Если month находится в списке зимних месяцев, выводим "Зима"
# TODO Добавьте блок else c обработкой некорректного номера месяца
