class Figure:
    side_count = 0
    filled = bool
    def __init__(self, __sides, __color):
        self.__sides = __sides
        self.__color = __color

    def get_color(self, r, g, b):
        self.__color = (r, g, b)
        return self.__color

    def __is_valid_color(self, r, g, b):
        if r and g and b in range(0, 256):
            r == self.__color
        else:
            print('Введите коректное значение RGB')

    def set_color(self, r, g, b):
        self.__is_valid_color(r, g, b)

    def __is_valid_sides(self, *args):
        self.args = int(args)
        if args > 0 and self.__sides == len(args):
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.args)

    def set_sides(self, *new_sides):
        if new_sides != self.side_count:
            new_sides = self.side_count
        else:
            self.side_count = self.side_count

class Circle(Figure):
    sides_count = 1
    def __init__(self):
        __radius = self.__sides

    def get_square(self):
        pass

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        pass

class Cube(Figure):
    side_count = 12
    __sides = ...

    def get_volume(self):
        pass
