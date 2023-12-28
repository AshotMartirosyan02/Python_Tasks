
from property import Property

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @Property
    def x(self):
        return self.__x

    @x.seter
    def x(self, value):
        if type(value) in (int, float):
            self.__x = value

        else:
            raise ValueError("Can be int or float")

    @Property
    def y(self):
        return self.__y

    @y.seter
    def y(self, value):
        if type(value) in (int, float):
            self.__y = value
        else:
            raise ValueError("Can be int or float")

    def __erkarutyun(self):
        return ((self.__x ** 2 + self.__y ** 2) ** 0.5)

    def __str__(self):
        return f"Vector {(self.__x, self.__y)}"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.__x + other.__x, self.__y + other.__y)
        else:
            raise ValueError("Your type not Vector")

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(self.__x * other.__x, self.__y * other.__y)
        elif isinstance(other, (int, float)):
            return Vector(self.__x * other, self.__y * other)
        else:
            raise ValueError("Your type not Vector")

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.__erkarutyun() == other.__erkarutyun()
        return False

    def __gt__(self, other):
        if isinstance(other, Vector):
            return self.__erkarutyun() > other.__erkarutyun()
        return False

    def __ge__(self, other):
        if isinstance(other, Vector):
            return self.__erkarutyun() >= other.__erkarutyun()
        return False

    def __lt__(self, other):
        if isinstance(other, Vector):
            return self.__erkarutyun() < other.__erkarutyun()
        return False

    def __le__(self, other):
        if isinstance(other, Vector):
            return self.__erkarutyun() <= other.__erkarutyun()
        return False


p1 = Vector(1, 2)
p2 = Vector(1, 5)
# p3 = Vector("2", 2)
print(p1<=p2)
