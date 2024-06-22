from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, colores):
        self.__sides = []
        self.__color = colores
        self.filled = False

    def get_color(self, *color):
        return self.__color

    def set_color(self, *color):
        if self.__is_valid_color(color):
            self.__color = color

    def __is_valid_color(self, *color):
        c = False
        if len(color) != 3:
            return False
        for i in color:
            if 0 <= i and i <= 255:
                c = True
        return c

    def set_sides(self, *sides, new=False):
        try:
            list1 = list(*sides)
        except:
            list1 = list(sides)
        if isinstance(self, Circle):
            if len(list1) == 1:
                self.__sides = list1  #list(sides)
            else:
                if new:
                    self.__sides = [1]
        elif isinstance(self, Triangle):
            if len(list1) == 3:
                self._Figure__sides = list1
            else:
                if new:
                    self.__sides = [1, 1, 1]
        elif isinstance(self, Cube):
            if len(list1) == 12:
                self.__sides = list1
            elif len(list1) == 1:
                self._Figure__sides = list1 * 12
            else:
                if new:
                    self._Figure__sides = [1] * 12
        else:
            pass

    def __is_valid_side(self, sides):
        if isinstance(self, Circle | Cube):
            if len(sides) == 1:
                return True
            else:
                return False
        elif isinstance(self, Triangle):
            if len(sides) == 3:
                return True
            else:
                return False
        return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        f = 0
        for i in self.__sides:
            f += i
        return f


class Circle(Figure):

    def __init__(self, colores, *sides):
        # if len(sides) == 0:
        #     return print("Пустой список сторон Circl")
        self.__radius = sides[0] / (2 * pi)  # 2 * pi * radius
        self.sides_count = 1
        super().__init__(colores)
        super().set_sides(*sides, new=True)

    def get_square(self):
        return pi * self._Circle__radius ** 2

    def get_perim(self):
        return 2 * pi * self._Circle__radius


class Triangle(Figure):
    __height = 0

    def __init__(self, colores, *sides):
        self.sides_count = 3

        super().__init__(colores)
        super().set_sides(sides, new=True)
        p = len(self) / 2
        self.__height = ((2 * sqrt(
            p * (p - self._Figure__sides[0]) * (p - self._Figure__sides[1]) * (p - self._Figure__sides[2])))
                         / self._Figure__sides[0])

    def get_square(self):
        sq = self.__height * self._Figure__sides[0] / 2
        return sq


class Cube(Figure):
    def __init__(self, colores, *sides):
        super().__init__(colores)
        super().set_sides(*sides, new=True)

    def get_volume(self):
        sid = self.get_sides()
        return 6 * sid[0] ** 2


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((155, 54, 98), 15, 25, 15)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

print("Проверка периметра (круга), это и есть длина:")
print(len(circle1))
print(f'периметр куба {len(cube1)}')
print(f'периметр треугольника : {len(triangle1)} ,его стороны : {triangle1.get_sides()}')
print(f" Проверка объёма (куба): {cube1.get_volume()}")
print(f"Проверка площадь треугольника : {triangle1.get_square()}")