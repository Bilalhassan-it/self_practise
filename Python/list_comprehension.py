# list comprehension = A concise way to create list, set, dict, generator
#                      in Python.
#                      Compact and easier to read than traditional loops
#                      [expression for value/item in iterable (if condition) ]

numbers = [1, -2, 3, -4, 5, 6, -7]

positiveNumbers = [num for num in numbers if num >= 0]
negativeNumbers = [num for num in numbers if num < 0]
evenNumbers = [num for num in numbers if num % 2 == 0]
oddNumbers = [num for num in numbers if num % 2 != 0]

# Traditional way
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

# Pythonic 
seq = [x**2 for x in range(1, 11)] 
print(seq)


# All comprehensions
seq1 = [x**2 for x in range(1, 11)] # list comprehension
seq2 = {x**2 for x in range(1, 11)} # set comprehension
seq3 = (x**2 for x in range(1, 11)) # generator comprehension
        # This creates a generator object. Python donot store it in memory
        # but it produces values on demand (lazily). 
        # Use next() function or iterator to get each value one by one
seq4 = {x : x**2 for x in range(1, 11)} # dictionary comprehension


# pairs = []
# for x in [1,2]:
#     for y in [3,4]:
#         pairs.append((x, y))

# pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
# print(pairs)