
from file_ops import write_data, read_data
from config import FILENAME
from count_words import count_words
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

    total_words = count_words(FILENAME)
    print(f"Количество слов в файле {FILENAME}: {total_words}")

if __name__ == "__main__":
    main()
