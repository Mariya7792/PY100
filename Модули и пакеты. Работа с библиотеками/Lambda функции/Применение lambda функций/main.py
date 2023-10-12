# Поиск самого длинного слова
words = ["apple", "banana", "orange", "watermelon"]
longest_word = max(words, key=len)
print(longest_word)  # "watermelon"

# Поиск самого младшего человека
people = [
    {"name": "John", "age": 25},
    {"name": "Emily", "age": 30},
    {"name": "Adam", "age": 20}
]

youngest_person = min(people, key=lambda p: p["age"])
print(youngest_person)  # {"name": "Adam", "age": 20}

# Сортировка по возрасту в порядке возрастания
people = [
    {"name": "John", "age": 25},
    {"name": "Emily", "age": 30},
    {"name": "Adam", "age": 20}
]

sorted_people = sorted(people, key=lambda p: p["age"])
print(sorted_people)  # [{"name": "Adam", "age": 20}, {"name": "John", "age": 25}, {"name": "Emily", "age": 30}]

# Сортировка по возрасту в порядке убывания
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90
}
sorted_students = dict(sorted(students.items(), key=lambda x: x[1], reverse=True))
print(sorted_students)  # {'Bob': 92, 'David': 90, 'Alice': 85, 'Charlie': 78}
