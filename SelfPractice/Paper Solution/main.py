x = 7
print(x//2,x/2)

a = [1,2,3]
b = [1,2,3]
print(a == b, a is b)

for n in range(4):
    print(n,"even"if (n & 1) == 0 else "odd")

numbs = [1,2,3]
sq=[n**2 for n in numbs]
print(numbs)
print(sq)

