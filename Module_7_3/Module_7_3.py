# Домашнее задание по теме "Оператор "with".
import string


class WordsFinder:
    def __init__(self, *input_list):
        self.file_names = []
        for file_name in input_list:
            self.file_names.append(file_name)
        self.result = {}
        # print(self.file_names)

    def get_all_words(self):
        for file in self.file_names:
            all_words = []
            with open(file, encoding='utf-8') as source:
                content = source.read().split('\n')
                for line in content:
                    line = line.translate(str.maketrans('', '', string.punctuation))
                    words_in_line = line.split(' ')
                    for word in words_in_line:
                        if word != '':
                            all_words.append(word.lower())
            self.result[file] = all_words
        return self.result

    def find(self, word):
        word_indexes = {}
        for file_name in self.result:
            if word.lower() in self.result[file_name]:
                word_indexes[file_name] = self.result[file_name].index(word) + 1
            else:
                # word hasn't found
                word_indexes[file_name] = -1
        return word_indexes

    def count(self, word):
        word_counts = {}
        for file_name in self.result:
            if word.lower() in self.result[file_name]:
                word_counts[file_name] = self.result[file_name].count(word)
            else:
                word_counts[file_name] = 0
        return word_counts


f1 = WordsFinder('test_file.txt', 'Rudyard Kipling - If.txt')

print(f1.get_all_words())
print(f1.find("text"))
print(f1.count("test"))
print(f1.find('if'))
print(f1.count('if'))
