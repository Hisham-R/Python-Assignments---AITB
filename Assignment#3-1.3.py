from math import pi
from msilib.schema import SelfReg

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def getLength(self):
        return self.length

    def setLength(self, length):
        self.length = length    

    def getWidth(self):
        return self.width

    def setWidth(self, width):
        self.width = width
    
    def getArea(self):
        Area = (self.width*self.length)
        return Area
    
    def getPerimeter(self):
        Perimeter = (self.length+self.width)
        return Perimeter

    
NewRectangle = Rectangle(10, 20)
print('Area = ',NewRectangle.getArea())
print('Perimeter = ',NewRectangle.getPerimeter())