# Домашнее задание по теме "Файлы в операционной системе".

import os
import time


os.chdir('../')
path = os.getcwd()

path_normalized = os.path.normpath(path)
print(path_normalized)

dir_size = 0
dirs_count = 0
files_count = 0

for dirpath, dirnames, filenames in os.walk(path_normalized):
    # print(dirpath, dirnames, filenames)
    print('*' * 30)
    # print(os.path.dirname(dirpath))
    print(f'Смотрим в каталоге {dirpath}')
    for dir in dirnames:
        print(f'Обнаружен каталог {dir}')
        dirs_count += 1
    for file in filenames:
        full_file_path = os.path.join(dirpath, file)
        file_size = os.path.getsize(full_file_path)
        file_time = time.gmtime(os.path.getmtime(full_file_path))
        file_time_string = f'{file_time[2]}.{file_time[1]}.{file_time[0]}'
        print(f'Обнаружен файл {file}, изменён {file_time_string}, размер: {file_size} байт')
        dir_size += file_size
        files_count += 1


print(f'Директорий {path_normalized} содержит {dirs_count} вложенных директориев, {files_count} файлов, общим объемом {dir_size} байт')
