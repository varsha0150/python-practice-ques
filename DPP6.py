# ans1
#  class Dog:
#     def __init__ (self,name):
#         self.name=name

# my_dog=Dog('Buddy')     
# print(my_dog.name)   

# ans2
# class Car:
#     def __init__(self,make,model):
#         self.make=make
#         self.model=model
# my_car=Car('TOYOTA' , 'COROLLA')
# print(my_car.make,my_car.model)        

# ans3
# class Person:
#     def __init__(self,name):
#         self.name=name
# p= Person("Alice")
# print(p.name)       

# ans4
# class calculator:
#     def add(self,a,b):
#         return a+b
# calc=calculator()
# print(calc.add(2,3))    

# ans5
# class circle:
# #     pi=3.14

# # print(circle.pi)

# #ans6
# class Book:
#     def __init__(self,title):
#         self.title=title

# my_book=Book('1984') 
# print(my_book.title)       

# #ans7
# 1#CREATE A CLASS WITH METHODS

# class Rectangle:
#   def __init__(self, width, height):
#    self.width = width
#    self.height = height


# def area(self):
#  return self.width*self.height
# def perimeter(self):
#  return 2*(self.width+self.height)

# rect = Rectangle(5, 10)

# print("Area:",rect.area() )
# print("Perimeter:", rect.perimeter())

# 2 INHERITANCE
# class Animal:
#    def speak(self):
#     return "Animal sound"
   

# class Dog(Animal):
#  def speak(self):
#    return "Bark"
# my_dog = Dog()
# print(my_dog.speak()) 

# 3POLYMORPHISM
# class Cat:
#  def speak(self):
#   return "Meow"
# class Dog:
#   def speak(self):
#    return "Woof"

# def animal_sound(animal):
#  print(animal.speak())

# my_cat = Cat()
# my_dog = Dog()
# animal_sound(my_cat)
# animal_sound(my_dog)

# STATIC METHODS
# class MathUtils:
#  @staticmethod
#  def add(a, b):
#   return a + b
# print(MathUtils.add(5, 10)) 