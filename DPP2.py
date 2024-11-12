# ans1 Write a Python program to check if a string is a palindrome (reads the same
#  forwards and backwards).
# str=input("enter a string:")
# if str==str[::-1]:
#     print("string is palindrome")
# else:
#     print("string is not palindrome")    


# ans2 Write a Python program to count the number of vowels in a given string.
# str=input("enter a string:")
# vowels="aeiouAEIOU"
# count=0
# for char in str:
#     if char in vowels:
#         count+=1
#         print("no. of vowels in a string:", count)

# ans3  Write a Python program to find the length of a given string without using the built-in len() function.
# str=input("enter a string:")
# count=0

# for i in str:
#      count+=1
#      print("length of a string is ",count)

# ans4  Write a Python program to convert a string to uppercase and lowercase.
# str=input("enter a string:")
# print(str.upper())
# print(str.lower())

# ans5 Write a Python program to find the first occurrence of a substring in a given string.
# str= 'my self varsha and my full name is varsha saxena'
# print(str.find('varsha'))

# ans6  Write a Python program to replace all occurrences of a word in a string with another word.
# str="myself varsha "
# print(str.replace("myself"," i'm "))

# ans7   Write a Python program to reverse a string.
# str="myself varsha "
# new_str=str[14:0:-1]
# print(new_str)

# ans8  Write a Python program to check if two strings are anagrams (contain the same characters in a different order).
# a='race'
# b='care'

# sorted_a=sorted(a)
# sorted_b=sorted(b)

# if len(a)==len(b):

#     if (sorted_a==sorted_b):
#         print('strings are anagram')
#     else:
#         ('strings are not anagram') 
# else:
#     print('strings are not anagram')          


# ans9  Write a Python program that takes a sentence as input and counts the number of words in it. A word is defined as
#  a sequence of characters separated by spaces.
# str=input("enter a sentence:")
# words=str.split()
# count=len(words)
# print('total words in a string are:',count)

# ans10 Write a Python program that takes a string as input and returns a new string where each word's
#  first letter is capitalized (also known as "title case"). For example, the input "hello world" should return "Hello World".
#  Consider edge cases like multiple spaces between words
# str=input("enter a sentence:")
# new_str=str.title()
# print(new_str)

