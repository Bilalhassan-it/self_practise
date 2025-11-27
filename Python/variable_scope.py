# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in  


# LOCAL ////////////////

def func1():
    x = 3
    print(x)

def func2():
    x = 2
    print(x)

func1()
func2()


# ENCLOSED ////////////////

# def func1():
#     x = 3
#     def func2():
#         print(x)
#     func2()

# func1()


# GLOBAL ////////////////

# def func1():
#     print(x)

# def func2():
#     print(x)

# x = 3

# func1()
# func2()

# BUILT-IN ////////////////

# from math import pi, e

# def func1():
#     a, b, c, d,   e = 1, 2, 3, 4,   5
#     print(a, b, c, d,   e)

# func1()