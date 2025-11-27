# default arguments = A default value for certain parameters 
#                     default is used when that arugment is omitted
#                     make your function more flexible, reduces # of arguments
#                     1. positional 2. default 3. keyword 4. arbitrary

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(f"${round(net_price(1000))}")
