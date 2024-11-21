class WordsFinder:
    file_name = []

    def __init__(self, *files):
        self.files = files
        self.file_name.append(files)

    def get_all_words(self):
        all_words = {}
        punct = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for item in self.file_name:
            with open(item, encoding='utf-8') as file:
                for index, lines in enumerate(item, start=1):
                    for p in punct:
                        if p in lines:
                            del p
                            all_words[item] = lines.split()
        return all_words

    def find(self, word):
        find_words = {}
        for item in self.file_name:
            find_words[item] = item.tell(word)
        return find_words

    def count(self, word):
        num_words = {}
        sum_words = 0
        for item in self.file_name:
            for word in item:
                if word in item:
                    sum_words += 1
                    num_words[item] = sum_words
        return num_words




finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего



