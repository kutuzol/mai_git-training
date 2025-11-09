import re
def count_words(filename):
    """Подсчитывает количество слов в текстовом файле, игнорируя знаки препинания."""
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    # Используем регулярку для поиска слов (буквы, цифры, подчеркивания)
    words = re.findall(r'\b\w+\b', text)
    return len(words)  # Возвращаем количество слов в файле

