# Iterables = an object/collection that can return its element one 
#             at a time, allowing it to be iterated over in a loop

# numbers = {"1", "2", "3", "4", "5"}

# for number in numbers:
#     print(number, end=" ")

dictn = {"A":1, "B":2, "C":3, "D":4}

for key, value in dictn.items():
    print(f"{key}: {value}")

