import copy

a = [[2, 3], [5, 76]]
# a1 =[2, 3, 4, 5, 6, 7]

b = a # reference
c = copy.copy(a) # shallow copy
d = copy.deepcopy(a) # deep copy

b[0][0] = 99
print(a)
print(c)
print(d)

