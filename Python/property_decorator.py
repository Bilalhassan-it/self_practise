# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefit: Add additional logic when read, write, or delete attributes
#             Gives you getter, setter, and deleter method

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    # @property decorator, first set the method as a property then automatically it
    #           converts to a Getter method, so no need to create getter method manually
 
    @property
    def width(self):
        return f"{self._width:.1f}cm"
    
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("The width can't be less than or equal to zero") 

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("The height can't be less than or equal to zero")

    @width.deleter
    def width(self):
        del self._width
        print("The width has been deleted!") 

    @height.deleter
    def height(self):
        del self._height
        print("The height has been deleted!")

    
rectangle = Rectangle(3, 4)

rectangle.width = 3
rectangle.height = 3

del rectangle.width
del rectangle.height

# print(rectangle.width)
# print(rectangle.height)
