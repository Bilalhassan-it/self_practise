import random

class IsMultiple:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def display(self):
        if self.n % self.m == 0:
            return print("True")
        else:
            return print("False")
        
        

    
    