# TODO реализовать функцию
def insert(list_values, value, index=0):
    return list_values[:index] + [value] + list_values[index:]

print(insert([1], value=0))  # [0, 1]
print(insert([0, 2], value=1, index=1))  # [0, 1, 2]
print(insert([0, 1, 2], value=3, index=3))  # [0, 1, 2, 3]
