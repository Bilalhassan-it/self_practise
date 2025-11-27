# Inheritance = Allows a class to inherit attributes and variables from another class
#               Helps code reusability and extensibility
#               class Child(Parent)
#               class Sub(Super)

class Animal:

    max_age = 100
    min_age = 1

    def __init__(self, name, age, is_alive=True):
        self.name = name
        self.age = age
        self.is_alive = is_alive

    def move(self):
        print(f"{self.name} is moving")

    def eat(self):
        print(f"{self.name} is eating")
    

class Cat(Animal):
    def speak():
        print(f"CAT speaks \"MEOW\"")

class Dog(Animal):
    def speak():
        print(f"DOG speaks \"WOAF\"")

class Goat(Animal):
    def speak():
        print(f"GOAT speaks \"BHAIIIIIII\"")


cat = Cat("German cat", 3)
dog = Dog("Scubbi Duu", 18)
goat = Goat("Bakra", 3)

cat.speak()