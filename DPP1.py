#ans 1 print numbers from 1 to 10 using for loop
# v=0 
# for i in range(0,10):      
# v+=1 
# print(v) 

#ans 1 print numbers from 1 to 10 using for loop
# for i in range(1,10): 
#  print(i) 


#ans2  calculate the sum of numbers from 1 to 10 using for loop
# sum=0 
# for i in range(0,10):      
# sum+=i 
# print(sum) 


#ans 3 print even numbers from 1 to 10 using for loop
# for i in range(2,11,2):     
# print(i) 


#ans4 print numbers in reverse from 1 to 10 using a for loop
# for i in range(10,0,-1):   
# print(i) 


#ans6 print characters of a string using a for loop 
# v="varsha" 
# for v in 'varsha': 
# print(v) 


#ans7 find the largest number in a list using a for loop
# l=[1,4,7,3,8,2,9,0,] 
# for max in l : 
# print(max) 


#ans8 find the average of a numbers in a list using a for loop
# l=[10,5,23,65,30] 
# avrg=0 
# for i in l: 
#     avrg=avrg+i/2 
#     print(avrg) 
 
#ans9 count the number of a vowels in a string using a for loop
# v= str(input("enter a string :")) 
# vowels=0 
# for i in v: 
#     if i in "aeiou": 
#         vowels=vowels+1 
#         print("no. of vowels in: ",v,"is",vowels) 
 
#output of ans9 
# enter a string :varsha 
# no. of vowels in:  varsha is 1 
# no. of vowels in:  varsha is 2 
 
     
#ans10 print a pattern of stars using nested for loop
# n=6 
# for i in range(1, n+1): 
#     print("*"*i) 
 
#ans10 print a pattern of stars using nested for loop
# n=6 
# for i in range(1, n+1): 
#     for j in range(i): 
#       print("*", end="") 
#     print() 
 
#ans11 find the factorial of a number using a while loop
# num=4 
# fact=1 
# while(num>0): 
#     fact=fact*num 
#     num=num-1 
#     print("factorial of a number :",fact) 
 
#ans12 find the first occurence of a number in alist using a while loop 
# l1=[2,5,7,5,4,2,2,6] 
# i=0 
# while i < len(l1): 
# print(l1[i]) 
# i+=1 


#ans13 calculate a sum of numbers from 1 to 100 using a while loop
# v=1 
# sum=0 
# # while v<=100:      
# sum=sum+v 
# v=v+1 
# print(sum) 


#ans 14 find all the prime numbers between 1 and 50 using nested for and if
# num=2 
# for i in range(2,50):          
# j=2 
# while(j<=(i/2)): 
# if(i%j==0): 
# break 
# j+=1          
# if(j>i/j): 
# print(i,'is a prime number') 



#ans15 print the fibonacci sequence upto 10th sequence
# num=int(input("enter a number : ")) 
# print("fibonacci series : ") 
# num1 =0 
# num2=1 
# count=0 
# print(num1,end=' ') 
# print(num2,end=' ') 
# while count < num:      
# result = num1 + num2 
# print(result,end=' ') 
# num1=num2 
# num2=result   
# count=count+1 


# ans 19 
# num=input('enter number:') 
# sum=0 
# for i in num: 
#     sum+=int(i)**3 
# if sum==int(num): 
#   print('armstrong number') 
# else: 
#     print('not a armstrong number')


# ans20 
# v= input('enter a month name : ') 
# if v=='january' and 'march' and 'may' and 'july' and 'august' and 'october' and 'december' : 
#     print ('this month has 31 days') 
# elif v== 'february': 
#     print('this month has 28 days') 
# elif v== 'april' and 'june' and 'september' and 'november' : 
#     print('this month has 30 days') 
# else : 
#     print('invalid month')