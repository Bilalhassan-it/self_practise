# Positional argument functions

def happy_birthday(name, age):
    print(f"Happy birthday {name}!")
    print(f"you are {age} years old")
    print(f"Happy birthday to you!")
    print()

happy_birthday("Shabo", 18)
happy_birthday("Dumba", 20)
happy_birthday("Khamba", 22)

print("################################# \n")

def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

print(create_name("muhammad", "shaban"))

