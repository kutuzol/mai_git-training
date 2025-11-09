
from file_ops import write_data, read_data
from config import FILENAME
from count_line import count_lines
def main():
    data = [
        "Строка 1: привет, Дорогой пользователь!)",
        "Строка 2: эта программа нужна для лабораторной по Git",
        "Строка 3:  В ней нет особого смысла, как и в жизни многих людей",
        "Строка 4: Это новая строка, раньше её не было"
    ]
    
    write_data(FILENAME, data)
    print("Данные записаны в файл.")
    
    print("Чтение данных из файла:")
    content = read_data(FILENAME)
    for line in content:
        print(line)

  # Используем новую функцию
    total_lines = count_lines(FILENAME)
    print(f"Всего строк в {FILENAME}: {total_lines}")


if __name__ == "__main__":
    main()
