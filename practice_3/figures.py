class Shape():
    def __init__(self, s):
        self.sides = s

    def __str__(self):
        return ("\nЭто фигура на плоскости.\nУ неё " + str(len(self.sides)) + " сторон(ы)")

    def area(self):
        return ("\nПлощадь фигуры невозможно определить\n")


class Rectangle(Shape):

    def __init__(self, s):
        super().__init__(s)

    def __str__(self):
        return ("\nЭто прямоугольник\nсо сторонами " + str(self.sides))

    def area(self):
        return ("\nПлощадь прямоугольника: " + str(self.sides[0] * self.sides[1]))


class Triangle(Shape):
    def __str__(self):
        return ("\nЭто тругольник\nсо сторонами " + str(self.sides))

    def area(self):
        return ("\nПлощадь треугольника: " + str(0.5 * (self.sides[0] * self.sides[1])))


class Square(Rectangle):
    def __init__(self, side):
        self.sides = [side, side, side, side]

    def __str__(self):
        return ("\nЭто квадрат\nсо сторонами " + str(self.sides))

    def area(self):
        return ("\nПлощадь квадрата: " + str(self.sides[0] * self.sides[1]))
