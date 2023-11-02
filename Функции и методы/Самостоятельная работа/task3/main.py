# TODO реализовать функцию count
def count(list_values, value):
    count = 0
    for i in list_values:
        if value == i:
            count += 1

    return count



list_items = [1, 2, "3", 1]
print(count(list_items, 1) == list_items.count(1))  # True
print(count(list_items, 3) == list_items.count(3))  # True
