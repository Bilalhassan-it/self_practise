# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. car, phone, pen, mouse, cup
#          you need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object 

from car import Car

car1 = Car("Mustang", 2025, 4000, True)
car2 = Car("Ford", 2024, 3000, False)
car3 = Car("Zonda", 2023, 2000, True)

car1.describe()
car2.describe()
car3.describe()
