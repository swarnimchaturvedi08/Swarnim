class College:
    pass


#attributes and methods
#a variable defined inside a class is called an attribute
#a variable defined inside a class is a method

class Animal:
    name = "Lion" #attribute
    print()
    def speak(): #method
        print("Lion's Roar")

#everything inside a class is initialized only a single time
#so that means everyline inside the class is going to get executed
#once 

#accessing attributes and methods

class Student:
    name = "Swarnim"
    def details():
        print("Hello his name is Swarnim")


#Access attribute

print(Student.name)
#access method
Student.details()

