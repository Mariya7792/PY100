# Обращение к элементам словаря с помощью метода
student_scores = {"John": 85, "Jane": 92, "Alice": 78}
print(student_scores.get("John"))  # 85
print(student_scores.get("Bob"))  # None

student_scores = {"John": 85, "Jane": 92, "Alice": 78}
# Итерирование по значениям словаря
for score in student_scores.values():
    print(score)

# Итерирование по парам ключ-значение словаря
for item in student_scores.items():
    print(item)
