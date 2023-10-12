heads = 35  # Общее количество голов
legs = 94  # Общее количество лап

for rabbits in range(heads + 1):
    for pheasants in range(heads + 1):
        total_legs = 4 * rabbits + 2 * pheasants
        if total_legs > legs:
            continue  # Пропускаем подсчет голов, если количество лап превышает допустимое
        if rabbits + pheasants == heads and total_legs == legs:
            print("Кролики:", rabbits)
            print("Фазаны:", pheasants)
