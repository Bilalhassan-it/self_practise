# class MyClass:

#     def __init__(self, value):
#         self._value = value

#     def show(self):
#         print(f"value is {self._value}")
#     """its getter"""
#     @property
#     def ten_value(self):
#         return 10* self._value 
#     """its setter for set any new value in aour class like a modiefying"""
#     @ten_value.setter
#     def ten_value(self, new_value):
#         self._value = new_value/10


# obj = MyClass(5)
# obj.ten_value = 10
# print(obj.ten_value)   # Output: 5
# obj.show()


"""INHERATANCE (parent ki sari chesn usky child mn ho skti hn or kuch extra apni bhi chesn ho skti hn )"""
"""PARENT"""
class Employee:

     def __init__(self, name, id):
         self._name = name
         self._id = id

     def showDetails(self):
          print(f"The Name Of Employee {self._name} is {self._id}")

"""CHILD"""
class Programmer(Employee):
    def showDress(self):
          print(f"The Dress is BLUE")          

e1 = Programmer("Kashan", 420)    
e1.showDetails()
e1.showDress()
e2 = Programmer("Aman", 430)    
e2.showDetails()
e2.showDress()
e3 = Programmer("Sudais", 440)    
e3.showDetails()
e3.showDress()