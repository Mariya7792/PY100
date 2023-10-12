import csv

filename = 'output.csv'
headers = ['First Name', 'Last Name', 'Age']  # Заголовок для CSV файла
data = [  # Данные для CSV файла
    ['John', 'Doe', 25],
    ['Jane', 'Smith', 30],
    ['Alice', 'Johnson', 28]
]

# Открытие файла для записи
with open(filename, 'w') as file:
    writer = csv.writer(file)

    # Запись заголовка
    writer.writerow(headers)

    # Запись данных
    writer.writerows(data)

# Открытие файла для чтения сsv строк
with open(filename) as file:
    reader = csv.reader(file)
    # Чтение данных
    for row in reader:
        print(row)

# Открытие файла для получения чтения словарей из сsv строк
with open(filename, 'r') as file:
    reader = csv.DictReader(file)

    # Чтение данных
    for row in reader:
        print(row['First Name'], row['Last Name'], row['Age'])
