# https://urban-university.ru/members/courses/course999421818026/20231116-0000domasnee-zadanie-po-teme-fajly-v-operacionnoj-sisteme-128744189494
import os
import time

directory = '.'  # Замените на путь к вашему каталогу
count_files = 0
for dirpath, dirnames, filenames in os.walk(directory, topdown=True):
    # dirpath - это строка, путь к каталогу
    # dirnames - это список имен подкаталогов в dirpath, исключая особые символы '.' и '..'.
    # filenames - это список имен файлов в dirpath (не-каталогов)
    print(f'В директории [{dirpath}] обнаружено {len(filenames)} файлов')
    count_files += len(filenames)
    for file in filenames:
        full_path = os.path.join(dirpath, file)
        file_time = os.path.getmtime(full_path)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))
        file_size = os.path.getsize(full_path)
        parent_dir = os.path.dirname(full_path)
        print(f'Родительская директория: {parent_dir}, Время изменения: {formatted_time}, Имя файла: {file}, '
              f'\tПуть: {full_path}, Размер: {file_size} байт, ')
print(f'всего файлов {count_files}')
