class Vehicle:    #Родительский класс
    __COLOR_VARIANTS = ['orange', 'purple', 'yellow']    
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power
    
    def get_model(self):    #Информация о модели
        return f'Модель: {self.__model}'

    def get_horsepower(self):    #Информация о мощности
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):    #Информация о цвете
        return f'Цвет: {self.__color}'

    def get_owner(self):    #Информация о владельце
        return f'Владелец: {self.owner}'

    def print_info(self):    #Вывод информации 
        print(f'{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\n{self.get_owner()}')

    def set_color(self, new_color):    #Проверка цвета со сменой регистра
        self.new_color = new_color
        for color in self.__COLOR_VARIANTS:
            color.lower()
            if color in self.__COLOR_VARIANTS:
                self.__color = new_color
            else:
                return f'Нельзя сменить цвет на {new_color}'

class Sedan(Vehicle):    #Дочерний класс
    __PASSENGER_LIMIT = 5


# Текущие цвета 
__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
