import threading
import time


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for num in range(1, word_count+1):
            file.write(f'Какое-то слово № {num}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file.name}')


start_time1 = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time1 = time.time()
print(f'Время выполнения программы: {end_time1 - start_time1} секунд')


start_time2 = time.time()
tread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
tread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
tread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
tread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
treads = [tread1, tread2, tread3, tread4]
for i in treads:
    i.start()

for tread in treads:
    tread.join()
end_time2 = time.time()
print(f'Время выполнения программы: {end_time2 - start_time2} секунд')
