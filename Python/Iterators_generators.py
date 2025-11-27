# Iterators (not Iterables): is an object that manages an iteration 
#                            through a series of values. 
#                            " i = iter(data) " 

# Generatos: the most convenient technique for creating iterators 
#            in Python is through the use of generators.


# Iterators
data = [1, 2]  # It produces an instance of list class
i = iter(data) # It produces an instance of list_iterator class
               # This iterator does not store its own copies of the 
               # list of elemtents  Instead, it maintains a current 
               # index into the original list
data.append(3)
data.append(4)
data.append(5)
print(next(i), next(i), next(i), next(i), next(i))

# Generators
def factors(n): # traditional function that computes factors
    for k in range(1, n+1):
        if n % k == 0: # divides evenly, thus k is a factor
            yield k # It tells the compilor, we are creating a 
                    # generator not a traditional function

for factor in factors(100):
    print(f"{factor} ", end=" ")

# Infact generators can produce an infinite series of values like 
# fibonnaci series. Main purpose of generators is to give the output 
# only when requested which saves memory and time. 

def fibonnaci():
    a = 0
    b = 1
    while True:
        yield a
        next = a + b
        a = b
        b = next
    
i = fibonnaci()
print(next(i))