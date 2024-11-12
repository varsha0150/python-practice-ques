# ans1  Write a Python function add_two_numbers(a, b) that takes two numbers as input and returns their sum.
# def add(a,b):
#     c= a+b
#     return c
# x=int(input('enter 1st no.='))
# y=int(input('enter 2nd no.='))
# z=add(x,y)
# print('sum of two numbers are =', z )

# ans2  Define a function find_maximum(a, b) that accepts two numbers and returns the larger number
# def find_maximum(a,b):
#     c=max(a,b)
#     return c
# x=int(input('enter 1st no.='))
# y=int(input('enter 2nd no.='))
# z=max(x,y)
# print('maximum of two numbers are =', z )

# ans3 Create a function is_positive(num) that checks if a given number is positive. The function should return True if the number is positive and False otherwise
# def is_positive(num) :
#   return num
# num=int(input('enter a positive number='))
# if num>0:
#     print('positive number')
# else:
#     print('negative number')    

# ans4  Write a function print_name(name) that takes a string name and prints "My name is [name]."
# def print_name(name):
#     return name
# name=input('enter your name')
# print(f'My name is {name}')

# ans5 Write a function square(x) that returns the square of a number x
# def square(x):
#     return x**2

# a=int(input("enter a number="))
# print("square of a number is=",a**2)

# ans6 Write a Python function find_greater_than(lst, n) that accepts a list lst of numbers and a number n. The function should return a new list containing only the numbers greater than n
# def find_greator_than(lst,n):
#     return[num for num in lst if num > n]

# lst=[4,7,12,2,10,25,6]
# n=int(input('enter a num'))
# greator_number=find_greator_than(lst,n)
# print(greator_number)

# ans7  Create a function count_vowels(s) that takes a string s as input and returns the number of vowels in the string
# def count_vowels(s):
#     vowels="aeiouAEIOU"
#     return sum(1 for char in s if char in vowels)

# s=input('enter a string=')
# str=count_vowels(s)
# print(str)

# ans8  Write a Python function factorial(n) that calculates and returns the factorial of a number n using recursion
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#      return n*factorial(n-1)
# n=6
# fact=factorial(n)
# print(fact)

# ans9 Write a Python function circle_area(radius) that takes the radius of a circle and returns the area of the circle. (Use the formula: Area = π × radius², assume π = 3.1416).
# def circle_area(radius):
#     pi=3.1416
#     area=pi*(radius**2)
#     return area

# radius=int(input("enter a radius of a circle="))
# area_of_circle=circle_area(radius)
# print(area_of_circle)

# ans10 Write a Python function monthly_payment(principal, rate, years) that calculates the monthly mortgage payment for a given principal loan amount, annual
#  interest rate, and loan term in years. Use the formula : principle*rate*((1+rate)**years)/((1+rate)**years)-1
# def monthly_payment(principle,rate,years):
#     payment=principle*rate*((1+rate)**years)/((1+rate)**years)-1
#     return payment
# principle=int(input('enter principle'))
# rate=int(input('enter rate'))
# years=int(input('enter years'))
# m =monthly_payment(principle,rate,years)
# print(m)