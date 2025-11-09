def count_lines(filename):
    """Подсчет количества строчек в файле - возвращаем по итогу число."""
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return len(lines)
