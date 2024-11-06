import math

class Shape():

    def area(self):
        return self.area

class Rectangle(Shape):
    def area(a, b):
        area = a * b
        return print(f'Площадь прямоугольника {area}')

class Circle(Shape):
    def area(r):
        area = math.pi * r ** 2
        return print(f'Площадь круга {area}')


Rectangle.area(5, 4)
Circle.area(4)