class Rectangle(object):
    def __init__(self, height=2, width=3):
        self.height = height
        self.width = width

    def findPerimeter(self):
        a = self.height
        b = self.width
        if (a <= 100) and (b <= 100):
            if (a == b):
                p = a * 4
            else:
                p = 2 * (a + b)
            return p
        else:
            return "Высота и ширина должны быть <= 100"

    def findSquare(self):
        a = self.height
        b = self.width
        if (a <= 100) and (b <= 100):
            if (a == b):
                s = a * a
            else:
                s = a * b
            return s
        else:
            return "Высота и ширина должны быть <= 100"

    def outputRectangle(self, p, s, userChoose=3):
        if (userChoose == 1):
            print(f"\nПлощадь прямоугольника: {s}")
            return 1
        elif (userChoose == 2):
            print(f"\nПериметр прямоугольника: {p}")
            return 1
        else:
            print(f"\nПлощадь прямоугольника: {s}")
            print(f"\nПериметр прямоугольника: {p}")
            return 1
