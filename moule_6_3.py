from random import randrange    #Импорт для кол-ва яиц


class Animal:   #Родительский класс
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    _cords = [0, 0, 0]

    def __init__(self, speed):
        self.speed = speed

    def move(self, dx, dy, dz):     #Функция перемещения по координатам
        self._cords = dx * self.speed, dy * self.speed, dz * self.speed
        if self._cords[2] < 0:
            print("It's too deep, i can't dive :(")
            self._cords = dx * self.speed, dy * self.speed, dz

    def get_cords(self):    #Функция определения координат после перемещения
        print(f'X:{self._cords[0]}, Y:{self._cords[1]}, Z:{self._cords[2]}')

    def attack(self):   #Функция определенипя действия в зависимости от уровня опасности
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        if self._DEGREE_OF_DANGER > 5:
            print("Be careful, i'm attacking you 0_0")

class Bird(Animal):     #Дочерний класс
    beak = True

    def lay_eggs(self):     #Функция выводящая случайное кол-во яиц
        random_eggs = randrange(1,4)
        print(f"Here are(is) {random_eggs} eggs for you")

class AquaticAnimal(Animal):    #Дочерний класс
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):      #Функция погружения
        x = list(self._cords)
        x[2] = -dz / 2
        if x[2] < 0:
            x[2] = 0
        self._cords = tuple(x)


class PoisonousAnimal(Animal):      #Дочерний класс
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):   #Класс наследник
    def speak(self):
        print('Click-click-click')


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
