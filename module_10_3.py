import threading
import random
from time import sleep


class Bank:
    balance = 0
    lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            transaction = random.randint(50, 500)
            self.balance += transaction
            print(f'Пополнение: {transaction}. Баланс:{self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(100):
            transaction = random.randint(50, 500)
            print(f'Запрос на {transaction}')
            if transaction <= self.balance:
                print(f'Снятие: {transaction}. Баланс:{self.balance}')
                self.balance -= transaction
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
