
def write_data(filename, lines):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')

def read_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines()]
