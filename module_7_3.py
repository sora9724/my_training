class WordsFinder:
    file_name = ()

    def __init__(self, *files):
        self.files = files
        self.file_name = files

    def get_all_words(self):
        all_words = {}
        words = []
        punct = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for item in self.file_name:
            with open(item, encoding='utf-8') as file:
                for word in file.read().split():
                    words.append(word.lower())
                for index, lines in enumerate(file, start=1):
                    for p in punct:
                        if p == lines:
                            p.replace('')
            all_words[item] = words
        return all_words

    def find(self, word):
        word = word.lower()
        find_words = {}
        for item in self.file_name:
            with open(item, encoding='utf-8') as file:
                a = file.read().split()
                for i in a:
                    if word == i:
                        find_words[item] = a.index(word) + 1
        return find_words


    def count(self, word):
        word = word.lower()
        num_words = {}
        sum_words = 0
        for item in self.file_name:
            with open(item, encoding='utf-8') as file:
                a = file.read().split()
                for i in a:
                    if word == i:
                        sum_words += 1
                        num_words[item] = sum_words
        return num_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
