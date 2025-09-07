"""NAME MANGLING"""
class student:
     def __init__(self):
         self._name = "bilal"  #public
         self.__name = "bilal"  #private
a = student()
#print (a._name )      #its correct to run 

"""but as we use this its wrong"""
#print(a.__name)       #cant access 

""" but we use this to acess private method or values """
print(a._student__name)

"""..................................................................................................................."""
# class Students:
#     def __init__(self):

#          self._name = "bilal"

#     def _funname(self):

#          return "UBIT"
    
# class Department(Students):
        
#          pass

# obj = Students()
# obj1 = Department()
# #print(dir(obj))         #1st type to find name mangling obj method pr jo jo method/variabl run ho skty hn wo bta dyga
# #print(obj.__dir__())   #2nd type // // //
# print (obj._name)
# print (obj._funname)
# print (obj1._name)
# print (obj1._funname)

"""..................................................................................................................."""

# class Students:
#     def __init__(self, name="bilal"):   # default value
#         self._name = name

#     def __funname(self):                # private method
#         return "UBIT"
    
#     def get_funname(self):              # public accessor
#         return self.__funname()
    
# class Department(Students):
#     pass

# obj = Students()
# obj1 = Department()

# print(obj._name)           # Works: bilal
# print(obj.get_funname())   # Works: UBIT
# print(obj1._name)          # Works: bilal
# print(obj1.get_funname())  # Works: UBIT
