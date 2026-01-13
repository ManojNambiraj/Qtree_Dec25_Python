# Abstraction

from abc import ABC, abstractmethod

class Shape(ABC):
   
    def area(self):     # @abstractmethod
        pass

class Rectangle(Shape):
    
    def area(self):
        print("Area = length * Breadth")

class Square(Shape):
    
    def area(self):
        print("Area = length * Breadth")

r = Rectangle()

r.area()
