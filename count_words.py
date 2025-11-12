import re

def count_words(filename):
    """Подсчитывает количество слов в текстовом файле, игнорируя знаки препинания."""
    word_count = 0
    pattern = re.compile(r'\w+')
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                words = pattern.findall(line)
                word_count += len(words)
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return 0
    except IOError as e:
        print(f"Ошибка при чтении файла {filename}: {e}")
        return 0
    return word_count


