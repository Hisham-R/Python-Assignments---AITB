#3.1 
# from traceback import print_tb

# def Vowel(char):
#     return char.lower() in ['a', 'e', 'i', 'o', 'u']

# def count_vowels(string, vowels):
#    if( vowels == 1):
#         return Vowel(string[vowels-1]);
#    return (count_vowels(string, vowels - 1) + Vowel(string [vowels - 1]));

# string = 'Celebration'
# print("Numbers of Vowels =",count_vowels(string, len(string)))

#3.2
# def sum_numbers(num):
#     if num <= 1:
#         return num 
#     return num + sum_numbers(num - 1)
# num = 5
# print(sum_numbers(num))

#3.3
# term = int(input("Enter number of terms: "))
# n1, n2 = 0 , 1
# sum = 0
# count = 1

# print("Fibonacci Sequence: ")
# while(count <= term):
#   print(sum)
#   count += 1
#   n1 = n2
#   n2 = sum
#   sum = n1 + n2

#3.4
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# if 200 in sample_dict.values():
#     print('200 present in a dict')

#3.5
# from math import pi
# from msilib.schema import SelfReg

# class Circle:
#     def __init__(self, radius = 1.0, color = 'red'):
#         self.radius = radius
#         self.color = color
    
#     def getRadius(self):
#         return self.radius

#     def setRadius(self, radius):
#         self.radius = radius
    
#     def getArea(self):
#         return pow(self.radius, 2) * pi
    
#     def getColor(self):
#         return self.color

#     def setColor(self, color):
#         self.color = color
    

# class Cylinder(Circle):
#     def __init__(self, height = 1.0):
#         self.height = height

#     def getHeight(self):
#         return self.height

#     def setHeight(self, height):
#         self.height = height

#     def getVolume(self):
#         return self.height

# NewCircle = Circle(10)
# print('Area = ', NewCircle.getArea())
# print('Radius = ', NewCircle.getRadius())
# print('Color = ', NewCircle.getColor())
