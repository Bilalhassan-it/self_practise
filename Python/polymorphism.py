# Polymorphism = Greek word that means "have many forms or faces"
#                Poly -> Many
#                Morhpe -> Forms / Faces

#                TWO WAYS TO CREATE POLYMORPHISM 
#                1. Inheritance = An object could be treated of the same type as a parent class
#                2. "Duck typing" = Object must have minimum necessary attributes/methods 
#                                   "If it looks like a duck and quacks like a duck, it must be a duck." 


# METHOD 1: Inheritance

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.147 * self.radius ** 2

class Square(Shape):
    def __init__(self, width):
        self.width = width

    def area(self):
        return self.width ** 2

class Triangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
         
# Pizza is Polymorphism who act as a pizza, circle, and a shape
class Pizza(Circle):
    def __init__(self, radius):
        super().__init__(radius)

# CheeseParatha is Polymorphism who act as a CheeseParatha, pizza, circle, and a shape
class CheeseParatha(Pizza):
    def __init__(self, radius):
        super().__init__(radius)

shapes = [Circle(4), Square(9), Triangle(6, 7), Pizza(4), CheeseParatha(4)]

for shape in shapes:
    print(shape.area())
  

# METHOD 2: "Duck typing"

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("The dog goes \"WOAF\"")

class Cat(Animal):
    def speak(self):
        print("The cat goes \"MEOW\"")

class Car:
    alive = True
    def speak(self):
        print("The car goes \"HONK\"")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)