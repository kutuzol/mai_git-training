
from file_ops import write_data, read_data
from config import FILENAME

def main():
    data = [
        "Строка 1: привет, Дорогой пользователь!)",
        "Строка 2: эта программа нужна для лабораторной по Git",
        "Строка 3:  В ней нет особого смысла, как и в жизни многих людей",
        "Строка 4: Это новая строка, раньше её не было"
    ]
    
    write_data(FILENAME, data)
    print("Данные записаны в файл.")
    

    content = read_data(FILENAME)
    print("Данные были считаны из файла...:")
    for line in content:
        print(line)

if __name__ == "__main__":
    main()
