import os


def exists_file(filename: str):
    """Проверка существования файла"""
    if os.path.exists(filename):
        print(f"Файл {filename} существует.")
    else:
        print(f"Файл {filename} не существует.")


if __name__ == '__main__':
    file = "output.txt"
    exists_file(file)

    print(f"Создание и запись в файл {file} ...")
    with open(file, "w") as f:  # TODO Добавьте аргумент encoding='utf-8'
        f.write("Hello, World!\n")  # Вручную нужно добавлять символ переноса строки, чтобы разделить файл на строки
        f.write("Python - замечательный язык программирования.\n")
        f.write("Работа с файлами в Python..\n")
    exists_file(file)

    print(f"Построчное чтение файла {file} ...")
    with open(file, "r") as f:
        for line in f:
            # Метод строки rstrip удаляет непечатаемые символы справа, чтобы не было двух символов переноса строки
            print(line.rstrip())   # Можно заменить на print(line, end="")
