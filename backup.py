# variables 
# name="krishna"
# age=302

#  1. do not give space while starting at the variable name
#  name="krishna"

# 2.variable name ke beech mai space nhi dena hai
# name surname="krishna"

# 3. do not use special character
# @name="krishna"


# output
# print(name,age)


# data types
# 1. numbers
# int 1,2,3,4,..
# number =100
# print(type(number))


# float decimal values or p/q 
# percentage =75.4
# a=10
# b=5
# print(type(a/b))

 
# complex 
# imaginary=10+ 10j
# print(type(imaginary))


# 2.string
# name="23@#$fjdvbn"
# print(type(name))

# name="swarnim"
# print(name)


# 3.boolean 
# True or False 
# truthy or falsy values 
# falsy values -->> 0,0.0,[],{},(),"",False,None
# print(bool(0))
# print(bool(0.0))
# print(bool(""))
# print(bool(" "))
# print(bool(0.1))
# print(bool([]))
# print(bool({}))
# print(bool(()))
# print(bool(False))
# print(bool(None))
# print(bool("age"))
# print(bool(18))



# indexing and slicing 
# indexing
# positive indexing 0,1,2,3,.... 
# name="python"
# print(name[3])
# print(name[4])
# print(name[0],name[5])


# negative indexing -1,-2,-3,....
# print(name[-1])


# slicing 
# start index : stop index: step value 
# positive slicing 
# name="sheryians"
# print(name[0:4:1])
# print(name[0:6:2])

# negative slicing 
# print(name[-1:-6:-1])
# print(name[::-1])


# input
# name=input("enter your naam : ")
# print(f"name : {name}")
# age =(input("enter your age : "))
# print(age)
# print(type(age))



# operators 
# arithmetic operators 
# +,-,/,//,*,**,%
a=10
b=3
# print(a+b)
# print(a-b)
# print(a/b)
# print(a*b)
# print(a**b)
# print(a//b)
# print(a%b)



# assignment operators 
# +=,-=,//=,/=,*=,**=,%=
# a=10
# a//=5
# print(a)

# comparison operator 
# ==,>,<,<=,>=,!=
# a=10
# b=10
# print(a!=b)
# print(a==b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)



# logical operators 
# and or not 
# and -->  in this we need every condition to be true 
# print((10==10 and 20>10) and 20>30)

# or->> if any one condition is true it will return true 
# print(10==20 or 10>20 or 20!=20)

# not  --> true ko false, false ko true
# print(not((10!=10 and 10==10) or 20>30 ))
# print(not(20!=20) and (2==4 or 2==2) and (not(10!=40)))


# if else 
# a=-19
# if a>0:
#     print("it is greater than 0 ")
# elif a==0:
#     print("it is equal to 0 ")
# else:
#     print("it is less than 0")


# even odd 
# n=int(input("enter your number : "))
# if n%2==0:
#     print(f"{n} is even number ")
# else:
#     print(f"{n} is odd number ")


# nested if else 
# check whether a num is +ve or -ve if +ve then check it is even or odd
# n=int(input("enter your number : "))
# if n>0:
#     if n%2==0:
#         print("+ve and even ")
#         if n%4==0:
#             print("+ve and divided by 2 and 4")
#         else:
#             print("+ve and divisble by 2 but not by 4")
#     else:
#         print("+ve and odd")
# else:
#     print("-ve")



# for loop 
# for i in range(1,11,1):
#     print(i)

# for i in range(10,0,-1):
#     print(i)

# n=int(input("enter your range : "))
# for i in range(1,n+1):
#     if i%2!=0:
#         print(i)


# n=int(input("enter your num :"))
# for i in range(n,(n*10)+1 , n):
#     print(i)


# 2*1=2
# 2*2=4
# 2*3=6


# n=int(input('enter your num : '))
# for i in range(1,11):
#     print(f"{n} * {i} ={n*i}")



# a="nature"
# for i in range(len(a)):
#     print(a[i])


# n=10
# sum=0 
# n=int(input("enter your number "))
# for i in range(1,n+1):
#     sum+=i
# print(sum)


# while loop 
# n=1
# while n<10:
#     print(n)
#     n+=1


# n=143
# while n!=0:
#     digit=n%10
#     print(digit)
#     n=n//10


# x*10+3 =3
# 3*10+4 
# 34*10+1

# n=12234
# rev=0
# while n!=0:
#     digit=n%10
#     n=n//10
#     rev=rev*10 + digit
# print(rev)


# n=1221
# rev=0
# copy=n
# while n!=0:
#     digit=n%10  #1  , 2 ,2 ,1 
#     n=n//10 #122 12 1  0
#     rev=rev*10 + digit
# if copy ==rev:
#     print('palindrome')
# else:
#     print("not palindrome")


# functions 
# def addition(a,b):
#     return a+b
# print(addition(10,20))
# print(addition(100,200))
# print(addition(20,50))


# def ispalindrome(n):

#     rev=0
#     copy=n
#     while n!=0:
#         digit=n%10  #1  , 2 ,2 ,1 
#         n=n//10 #122 12 1  0
#         rev=rev*10 + digit
#     if copy ==rev:
#         return ('palindrome')
#     else:
#         return ("not palindrome")
# print(ispalindrome(1222))


# list 
# arr_123=[10,20,30,40,60]
# for i in range(len(arr_123)):
#     print(arr_123[i])


# for i in arr_123:
#     print(i)

# a=20
# arr=[10,20,30,40]
# for i in range(len(arr)):
#     if arr[i]==a:
#         print(i)

# largest=0 #20 #80 #100
# arr=[20,80,100,60]
# for i in arr:
#     if i >largest:
#         largest=i
# print(largest)