#6.  .update() -> to merge two dictionary
# a = {"Ravi" : 80, "Devraj" :23}
# b = {"Tanishq" :80, "Akarsh" :101}
# a.update(b)
# print(a)

#7. len() -> length of dictionary (total number of keys.)
# d = {1:10, 2:20 ,3:30,4:40,5:50}
# print(len(d))


# Question print each key
# d= {"Ravi" : 80,"Rohan" : 33,"chirag":22,"Devraj":100}
# method 1
# print(d.keys())
# method 2
# for i in d:
#     print(i)

# method 3
# for key,value in d.items():
#     print(key)

# Question Print student who scored more than 80
# d= {"Ravi" : 80,"Rohan" : 33,"chirag":22,"Devraj":100}
# for name , marks in d.items():
#     if marks>=80:
#          print (name,marks)

# Question 4 find and print the student with the highest marks using the for loop 
# d= {"Ravi" : 80,"Rohan" : 33,"chirag":22,"Devraj":100}
# highest=0
# for name,marks in d.items(): 
#     if marks > highest:
#         highest=marks
#         top=name
#     print(top)
#     print(highest)


# Question  Create a dictionary of numbers and their square from (1 to 5):


# square = {}
# for i in range (1,6):
#     square [i] = i*i
# print(square) 

# Que. Add 5 bonus marks to every student
# d= {"Ravi" : 80,"Rohan" : 33,"chirag":22,"Devraj":100}
# for i in d:
#     d[i] = d[i] + 5
# print(d)