import random
from threading import Thread
from time import sleep
from queue import Queue


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        sleep(random.randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        list_guests = list(guests)
        for i in range(len(self.tables)):
            thread = list_guests[i]
            thread.start()
            print(f'Гость {list_guests[i].name}, сел за стол номер {self.tables[i].number}')
        if len(list_guests) > len(self.tables):
            for i in range(len(self.tables), len(list_guests)):
                self.queue.put(list_guests[i])
                print(f'{list_guests[i].name} в очереди')


    def discuss_guests(self):
        while not self.queue.empty() or Cafe.check_table(self):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name}, покушал(-а) и ушел(ушла)')
                    table.guest = None
                    print(f'Стол номер {table.number} свободен')
                if table.guest is None and not self.queue.empty():
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    thread = table.guest
                    thread.start()

    def check_table(self):
        for i in self.tables:
            if i.guest is None:
                return False
            return True

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
