# *args    (tuple) = allows you to pass multiple non-key arguments
# **kwargs (dict)  = allows you to pass multuple keyword arguments
#                    * unpacking operator
#                    These areARBITRARY ARGUMENTS

def add(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add(1, 2, 3, 4, 5))

###########################################3

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(pakistan="Islamabad", 
              India=5,
              USA="New York",
              China="Muan")