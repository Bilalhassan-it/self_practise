# class variables = variables shared among all instaces of a class 
#                   Defined outside the constructor
#                   Allow you to share data among all instances created from that class

class Student:

    batch = 2025
    num_students = 0

    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
        Student.num_students += 1

def identity(self):
    print(f"{self.name} has {self.gpa} gpa and is {self.age} years old")

    
student1 = Student("Spongebob", 20, 3.3)
student2 = Student("Sandy", 18, 4)
student3 = Student("Squidward", 40, 3.8)
student4 = Student("Patrick", 30, 2.8)

print(f"My {Student.batch} batch class has {Student.num_students} students: ")

print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

