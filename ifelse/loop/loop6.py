# n = int(input("Enter Your Number:-"))

# sum = 0
# temp = n


# while n !=0:
#     z = n% 10
#     fact=1
#     for i in range (1,z+1):
#         fact=fact*i

#         sum = sum+fact


#         n = n//10

# if sum == temp:
#     print("Strong Number")
# else:
#     print("Not strong Number")



import random

num = random.randint(1, 100)

print("Guess the number between 1 and 100")

guess = int(input("Enter your guess:"))

while guess != num:

    if guess < num:
        print("Thoda upar aa neech.")
    else:
        print("Thoda neeche aao maalik,Jannat hai.")

    guess = int(input("Enter your guess:"))

print("Congratulations! You guessed the number.")




