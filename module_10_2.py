import threading
import time


class Knight(threading.Thread):     # Создание класса
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.army = 100
        self.days = 0

    def fight(self):
        while self.army:
            time.sleep(1)
            self.days += 1
            print(f'{self.name}, Сражается {self.days} день(дня)... осталось {self.army - self.power} воинов\n')
            self.army -= self.power
            if self.army == 0:
                print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.fight()


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()    # Запуск потоков
second_knight.start()
first_knight.join()     # Остановка потоков
second_knight.join()
if first_knight.is_alive() == False and second_knight.is_alive() == False:
    print('Все битвы закончились!')     # Вывод строки об окончании сражения
