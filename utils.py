import os


def delete_files_recursive(folder_path, file_list):
    for root, dirs, files in os.walk(folder_path):
        if not root.endswith("tests"):
            for file in files:
                if file in file_list:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    print(f"Удален файл: {file_path}")


if __name__ == '__main__':
    folder_path = os.getcwd()
    files_to_delete = ["output.txt", "output.json", "output.csv"]

    delete_files_recursive(folder_path, files_to_delete)
