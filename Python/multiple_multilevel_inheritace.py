# multiple inheritace = inherit from more than one classes 
#                       C(A, B)

# multilevel inheritance = inherit from parent which inherits from another parent


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def drink(self):
        print(f"{self.name} is drinking")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Cheel")
fish = Fish("Nemo")

hawk.sleep()
