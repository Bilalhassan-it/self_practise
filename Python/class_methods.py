# Class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself

# Class methods = Best for class-level data or require access to the class itself

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total # of students are {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        return f"The total gpa of {cls.count} students is {cls.total_gpa / cls.count :.2f}"

student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.2)
student3 = Student("Sandy", 4)

print(Student.get_count())
print(Student.get_average_gpa())
