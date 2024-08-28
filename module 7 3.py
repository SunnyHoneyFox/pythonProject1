import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = file.read().lower().translate(str.maketrans('', '', string.punctuation)).split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        result = {}
        for file_name, words in self.get_all_words().items():
            try:
                index = words.index(word.lower())
                result[file_name] = index + 1
            except ValueError:
                pass
        return result

    def count(self, word):
        result = {}
        for file_name, words in self.get_all_words().items():
            count = words.count(word.lower())
            if count > 0:
                result[file_name] = count
        return result


finder = WordsFinder('test_file.txt',
                     'Rudyard Kipling - If.txt',
                     'Mother Goose - Monday’s Child.txt')
print(finder.get_all_words())
print(finder.find('for'))
print(finder.count('for'))
