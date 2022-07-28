from math import pi
from msilib.schema import SelfReg

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius

    def getArea(self):
        return pow(self.radius, 2) * pi

    def getCircumfe(self):
        Circum = 2*pi*self.radius
        return Circum
    
NewCircle = Circle(10)
print('Area = ',NewCircle.getArea())
print('Circumference = ',NewCircle.getCircumfe())