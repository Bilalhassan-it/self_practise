# super() = Function used in a child class to call methods from parent class (super class)
#           Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, is_fill, has_border):
        self.color = color
        self.is_fill = is_fill
        self.has_border = has_border

    def get_color(self):
        return self.color
    
    def get_is_fill(self):
        return self.is_fill
    
    def get_has_border(self):
        return self.has_border
    
    
    def set_color(self, color):
        self.color = color
        
    def set_is_fill(self, is_fill):
        self.is_fill = is_fill

    def set_has_border(self, has_border):
        self.has_border = has_border


    def describe(self):
        print(f"It has {self.color} {'filled' if self.is_fill else 'unfilled'} color and has {'border' if self.has_border else 'no border'}")

class Circle(Shape):
    def __init__(self, color, is_fill, has_border, radius):
        super().__init__(color, is_fill, has_border)
        self.radius = radius

    def describe(self):
        print(f"This Circle has a radius of {self.radius}cm^2")
        super().describe()

    def get_radius(self):
        return self.radius
    
    def set_radius(self, radius):
        self.radius = radius

class Square(Shape):
    def __init__(self, color, is_fill, has_border, width):
        super().__init__(color, is_fill, has_border)
        self.width = width

    def describe(self):
        print(f"This Square has a width of {self.width}cm")
        super().describe()

    def get_width(self):
        return self.width
    
    def set_width(self, width):
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_fill, has_border, width, height):
        super().__init__(color, is_fill, has_border)
        self.width = width
        self.height = height

    def describe(self):
        print(f"This Triangle has a width and height of {self.width}cm and {self.height}cm")
        super().describe()

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height


circle = Circle(color="Red", is_fill=True, has_border=False, radius=5.3)
square = Square(color="Blue", is_fill=False, has_border=True, width=10)
triangle = Triangle(color="Green", is_fill=True, has_border=False, width=3, height=9)

triangle.set_color("Purple")
triangle.set_is_fill(False)
triangle.set_has_border(True)
triangle.set_width(90)
triangle.set_height(30)

print(triangle.get_color(),
      triangle.get_is_fill(),
      triangle.get_has_border(),
      triangle.get_width(),
      triangle.get_height())

triangle.describe()
# print()
# square.describe()
# print()
# triangle.describe()
