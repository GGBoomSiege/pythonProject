import os
import os.path

def read_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        return None

if __name__ == '__main__':
    content = read_file('./data/code.txt')
    print(content)