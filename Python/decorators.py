# Decorators = A function that extends the behaviour of another function
#              without modifying the base function

#              Pass the base function as an argunment to the decorator

def add_sprinkles(base_func):
    def wrapper(*args, **kwargs):
        print("You add sprinkles 🎆")
        base_func(*args, **kwargs)
    return wrapper

def add_fudge(base_func):
    def wrapper(*args, **kwargs):
        print("You add fudge 🍫")
        base_func(*args, **kwargs)
    return wrapper


@add_fudge
@add_sprinkles
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream")

get_ice_cream("Shahi Kulfa")