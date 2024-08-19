# Домашнее задание по теме "Позиционирование в файле".

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    string_positions = dict()
    string_no = 0
    for string in strings:
        string_no += 1
        string_positions[(string_no, file.tell())] = string
        file.write(string + '\n')
    return string_positions


strings = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]
result = custom_write('test.txt', strings)
for elem in result.items():
    print(elem)
