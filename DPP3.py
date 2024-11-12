# LIST ANSWERS
# ans1  Basic List Creation: Create a list of 5 integers and print the sum of all the elements
#  int_list =[1,2,3,4,5]
# sum=0
# for i in int_list:
#     sum+=i
#     print(sum)

# ans2  Indexing: Given the list numbers = [3, 8, 2, 10, 6], print the first, last, and  middle elements of the list.
# numbers = [3,8,2,10,6]
# print(numbers[0:5:2])
# first_num=numbers[0]
# middle_num=numbers[2]
# last_num=numbers[4]
# print('first num : ',first_num)
# print('middle no. : ', middle_num)
# print('last no. : ',last_num)

# #ans3 Slicing: For the list fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry'], slice the list to print the first three elements.
# fruit=['apple', 'banana' , 'cherry' , 'date' , 'elderberry']
# print(fruit[0:3])

# ans4  List Methods: Given the list colors = ['red', 'green', 'blue'], add 'yellow' t the end of the list and then remove 'green'
# colors=['red' , 'green' , 'blue']
# colors.append('yellow')
# print(colors)
# colors.remove('green')
# print(colors)

# ans5 List Comprehension: Generate a list of squares of numbers from 1 to 10 using list comprehension.
# square=[x**2 for x in range(1,11)]
# print(square)

# ans6  Nested List: Create a 2D list representing a 3x3 matrix and access the element in the second row and third column
# TWO_D_list=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# MATRIX=TWO_D_list[1][2]
# print(MATRIX)

# TUPLE ANSWERS

# ANS1 Basic Tuple Creation: Create a tuple of 4 strings and print its second element
# tup=('a','b','c','d')
# tup1=tup[1]
# print(tup1)

# #ans2 Immutability: Why can’t we modify the elements of a tuple? Demonstrate an example of an error that occurs when trying to modify a tuple.
# tup=('a','b','c','d')
# tup[1]='V'
# print(tup)
# output=TypeError: 'tuple' object does not support item assignment

# ans3  Tuple Unpacking: Given the tuple coords = (3, 5, 7), unpack the tuple into three variables and print each one.
# coords=(3,5,7)
# a,b,c=coords
# print(a,b,c)

# ans4 Tuple Concatenation: Concatenate two tuples (1, 2, 3) and (4, 5, 6) and print the result.
# tup1=(1,2,3)
# tup2=(4,5,6)
# tuple=tup1+tup2
# print(tuple)

# ans5 . Conversion: Convert the list [10, 20, 30] into a tuple and print the resulting tuple.
# list=[1,2,3]
# tup=tuple(list)
# print(tup)

# ans6   Finding Elements: Given the tuple letters = ('a', 'b', 'c', 'd'), check if the element 'e' is present in the tuple and print a message accordingly
# letters=('a','b','c','d')
# if 'e' in letters:
#     print ('e is present')
# else:
#    print ('e is absent')    

# DICTIONARY ANSWERS

# #ans1 Basic Dictionary Creation: Create a dictionary where the keys are fruits and the values are their prices. Print the price of an 'apple'
# fruits={'mango':10,'apple':12,'cherry':20,'strawberry':25}   
# print(fruits['apple'])

# ans2 Adding and Modifying Entries: Add a new entry 'orange': 30 to the dictionary {'apple': 50, 'banana': 20} and modify the price of 'banana' to 25.
# fruits={'mango':10,'apple':50,'banana':20,'strawberry':25}   
# fruits['orange']=30
# print(fruits)
# fruits['banana']=25
# print(fruits)

# ans3 Accessing Keys and Values: Given the dictionary student = {'name': 'John', 'age': 22, 'course': 'Computer Science'}, print all the keys and values.

# students= {'name':'john', 'age':22, 'course':'computer science'}
# for key,value in students.items():
#     print(key, ':',value)

# ans4 Dictionary Methods: Use the .get() method to safely access the price of 'grape' from the dictionary {'apple': 50, 'banana': 20, 'orange': 30}
# fruits= {'apple':50,'banana':20,'orange':30}  
# grape_price=fruits.get('grape')
# print(grape_price)

# ans5 Dictionary Iteration: Write a loop to iterate over the dictionary {'A': 90, 'B': 80, 'C': 70} and print each key-value pair.
# dict={'A':90,'B':80,'C':70}
# for key,value in dict.items():
#     print(key,':',value)

# ans6 Dictionary Comprehension: Create a dictionary where the keys are numbers from 1 to 5 and the values are their squares using dictionary comprehension
# d={x:x**2 for x in range(1,6)}
# print(d)

# WORD PROBLEMS
# ans1 Easy Level (Shopping List): You have a list of items you want to buy from the market:
#  ['apple', 'banana', 'milk', 'bread', 'eggs']. Write a program that adds
#  'chocolate' to the end of your shopping list and removes 'milk'. Finally, print the updated
#  shopping list

# shopping_list=['apple','banana','milk','bread','eggs']
# shopping_list.append('chocolate')
# print(shopping_list)
# shopping_list.remove('milk')
# print(shopping_list)

# ans2Mid Level (Student Grades): You are given a list of tuples where each tuple contains a
#  student's name and their score on a test:
#  students = [('Alice', 85), ('Bob', 90), ('Charlie', 78),('David', 92)].
#  Write a program that converts this list into a dictionary where the student's name is the
#  key and their score is the value. Then, print the names of students who scored above 80


# students=[('Alice',85),('Bob',90),('Charlie',78),('David',92)]
# dict={name: score for name , score in students}
# print(dict)

# for name , score in dict.items():
#     if score>80:
#         print(name,score)