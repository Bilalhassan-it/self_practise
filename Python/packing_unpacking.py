# Packing of expression: If a series of comma seperated expression is 
#                        given in a larger context then it will be 
#                        treated as a single tuple even if no enclosing 
#                        paranthesis are provided.

# UnPacking of expression: Python can automatically unpack a sequence 
#                          allowing one to assign series of identifiers
#                          to the given elements of sequence


# Packing of expression
data = 3, 4, 5, 6, 7, 8    # no need to enclose paranthesis.
print(data)

# UnPacking of expression
dict = {"Pakistan":92, "India": 91, "China":90, "UAE":180, "USA":1}
for key, value in dict.items():
    print(f"{key}: {value}")

for x, y in [(1, 2), (3, 4), (6, 7)]:
    print(f"(x, y) = {x},{y}")

a, b, c, d = range(7, 11) # implicitly not explicitly 

quotient, remainder = divmod(a, b)

