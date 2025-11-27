# Static methods = A method that belong to a class rather than any object of that class (Instance)
#                  Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (Object)
# Static methods = Best for utility functions that do not need access to class data
# Class methods = Best for class-level data or require access to the class itself

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} is a {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["CEO", "Manager", "Lead", "Senior", "Junior"]
        return f"You are the {position}" if position in valid_positions else "Position NOT found!"
    
employee1 = Employee("Spongebob", "Chef")
employee2 = Employee("Patrick", "Chef Assistant")
employee3 = Employee("Squidward", "Chashier")

print(Employee.is_valid_position("Junior"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())

