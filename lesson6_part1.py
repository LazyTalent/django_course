from math import pi


# task 1
class Apple:
    def __init__(self, cultivar="Adams Pearmain", size="1", color="red", country="England"):
        self.country = country
        self.color = color
        self.size = size
        self.cultivar = cultivar

    def __str__(self):
        return f"The cultivar is {self.cultivar}; Size = {self.size}; Color is {self.color}; From {self.country}"


# task 2
class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return pi * self.radius**2


# task 3
class Person:
    def __init__(self, name, surname, qualification=1):
        self.name = name
        self.surname = surname
        self.qualification = qualification

    def __str__(self):
        return f"{self.name} {self.surname}, qualification = {self.qualification}"


# task 4 (exception)
class WrongTriangleError(Exception):
    def __init__(self, expression, message):
        self.message = message
        self.expression = expression


# task 4 (main)
class Triangle:
    def __init__(self, a=1, b=1, c=1):
        self.a = a
        self.b = b
        self.c = c
        self.check_sides()

    def check_sides(self):
        sum_list = [self.a + self.b, self.b + self.c, self.a + self.c]
        for side in (self.a, self.b, self.c):
            for pair in sum_list:
                if pair < side:
                    raise WrongTriangleError(expression=(self.a, self.b, self.c), message="Bad triangle sides")

    def area(self):
        p = (self.a + self.b + self.c) / 2
        area = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** (1/2)
        return area


# task 5&6 (exceptions)
class WrongRectangleSides(Exception):
    def __init__(self, expression, message):
        self.message = message
        self.expression = expression


# task 5&6 (main)
class Rectangle:
    def __init__(self, a=1, b=1, c=1, d=1):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.check_sides()

    def check_sides(self):
        if self.a != self.c or self.b != self.d or self.a < 0 or self.b < 0 or self.c < 0 or self.d < 0:
            raise WrongRectangleSides(expression=(self.a, self.b, self.c, self.d), message="Bad rectangle sides")

    def calculate_perimeter(self):
        return sum((self.a, self.b, self.c, self.d))


class Square(Rectangle):
    def __init__(self, side=1):
        super(Square, self).__init__(side, side, side, side)

    def change_size(self, value):
        self.a += value
        self.b += value
        self.c += value
        self.d += value
        for side in (self.a, self.b, self.c, self.d):
            if side < 0:
                raise WrongRectangleSides(expression=(self.a, self.b, self.c, self.d), message="Bad rectangle sides")


def main():
    apple = Apple(country="Ireland")
    print("Task 1:", apple)
    circle = Circle(radius=3)
    print(f"Task 2: Radius = {circle.radius}; Area is {circle.area():.2f}")
    person = Person(name="Garret", surname="Crudelly")
    print(f"Task 3: {person}")
    print("\n\nTask 4 started:\n--------------------------------------------------")
    try:
        triangle = Triangle(a=2, b=3, c=40)
        print(f"Triangle with sides {(triangle.a, triangle.b, triangle.c)} has area = {triangle.area():.2f}")
    except WrongTriangleError as wte:
        print(f"{wte.expression} are {wte.message}")
    try:
        triangle = Triangle(a=2, b=3, c=4)
        print(f"Triangle with sides {(triangle.a, triangle.b, triangle.c)} has area = {triangle.area():.2f}")
    except WrongTriangleError as wte:
        print(f"{wte.expression} are {wte.message}")

    print("---------------------------------------------------------------\nTask 4 finished\n\n")
    print("Tasks 5&6 started:\n--------------------------------------------------")
    try:
        rectangle = Rectangle(1, 2, -1, 2)
        square = Square(side=5)
        print(f"Rectangle with sides {(rectangle.a, rectangle.b, rectangle.c, rectangle.d)} has perimeter = {rectangle.calculate_perimeter()}")
        print(f"Square with side {square.a} has perimeter = {square.calculate_perimeter()}")
    except WrongRectangleSides as wrs:
        print(f"{wrs.expression} are {wrs.message}")

    try:
        rectangle = Rectangle(1, 2, 1, 2)
        square = Square(side=5)
        print(f"Rectangle with sides {(rectangle.a, rectangle.b, rectangle.c, rectangle.d)} has perimeter = {rectangle.calculate_perimeter()}")
        print(f"Square with side {square.a} has perimeter = {square.calculate_perimeter()}")
        value = 2
        square.change_size(value)
        print(f"After increasing square side by {value}, square has perimeter = {square.calculate_perimeter()}")
    except WrongRectangleSides as wrs:
        print(f"{wrs.expression} are {wrs.message}")
    print("--------------------------------------------------\nTasks 5&6 finished")


if __name__ == "__main__":
    main()


