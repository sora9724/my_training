from random import choice


'''Lambda-функция'''

first = 'Мама мыла раму'
second = 'Рамена мало было'

a = list(map(lambda first, second: first == second, first, second ))
print(a)    #Проверка работы Lambda-функции


'''Замыкание'''

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for item in data_set:
                file.write(f"{item}\n")
    return write_everything

write = get_advanced_writer('example.txt')  #Проверка замыкания при записи в файл
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


'''Метод __call__'''

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self, *args, **kwargs):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное') #Проверка работы метода __call__
print(first_ball())
print(first_ball())
print(first_ball())
