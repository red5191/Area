import math
import abc


class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self): pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.width = w
        self.height = h
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, r):
        self.radius = r
    def area(self):
        return math.pi * self.radius ** 2


rect1 = Rectangle(3, 4)
print(f'Площадь прямоугольника {rect1.area()}')
circl1 = Circle(4)
print(f'Площадь круга {circl1.area()}')