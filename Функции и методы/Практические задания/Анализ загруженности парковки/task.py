# TODO Напишите функцию `calculate_parking_load`
def calculate_parking_load(total_parking_spaces, occupied_parking_spaces):
    parking_load = round(occupied_parking_spaces / total_parking_spaces * 100)
    if occupied_parking_spaces > total_parking_spaces:
        return False
    return parking_load


parking = calculate_parking_load(150, 100)
print(parking)
