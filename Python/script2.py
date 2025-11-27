from script1 import *

def favouriteDrink(drink):
    print(f"Your favourite drink is {drink}")

def main():
    print("This is script2")
    favouriteDrink("Water")
    favouriteFood("Burger")
    print("Good bye")

if __name__ == '__main__':
    main()

