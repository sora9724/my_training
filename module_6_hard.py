class Figure:
    side_count = 0
    filled = False

    def __init__(self, __color, __sides):
        self.__color = __color
        self.__sides = __sides

    def get_color(self):
        print (self.__color)

    def __is_valid_color(self, r, g, b):
        if r in range(0, 256) and g in range(0, 256) and b in range(0, 256):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) == True:
            self.__color = [r, g, b]
        else:
            self.__color = self.__color

    def __is_valid_sides(self, *args):
        if args > 0 and args == int and self.side_count == len(args):
            return True
        else:
            return False

    def get_sides(self):
        print(self.__sides)

    def __len__(self):
        print (self.__sides * self.side_count)

    def set_sides(self, *new_sides):
        if len(new_sides) != self.side_count:
            new_sides = self.side_count
            return new_sides
        else:
            self.side_count = self.side_count



class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, __sides):
        super().__init__(__color, __sides)
        self.__sides = __sides

    def radius(self):
        __radius = self.__sides / (2 * 3.14)
        return __radius

    def get_square(self):
        s = (self.__radius * 3.14) ** 2
        return s

    def __len__(self):
        return self.__sides


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, __sides):
        super().__init__(__color, __sides)
        self.__sides = __sides

    def get_square(self):
        p = 0.5 * self.__sides
        s = (p * (p - self.__sides) * (p - self.__sides) * (p - self.__sides)) ** 0.5
        return s

class Cube(Figure):
    side_count = 12

    def __init__(self, __color, __sides):
        super().__init__(__color, __sides)
        self.__sides = __sides


    def get_volume(self):
        v = self.__sides ** 3
        return v




circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
