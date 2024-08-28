# Project Title: Number Classification Program
# Objective:
# Your task is to develop a Python program that can determine whether a number is even, odd, or prime. The program should offer two options for the user:
# Option 1:
# The user enters a single number, and the program checks if the number is even, odd, or prime.
# Option 2:
# The user provides a list of numbers (up to 50 or 100). The program will:
# Identify and count how many numbers are even.
# Identify and count how many numbers are odd.
# Identify and count how many numbers are prime.
# Display the specific even, odd, and prime numbers along with their counts.
# Project Requirements:
# Program Functionality:
# Present the user with two options upon running the program.
# Analyze individual numbers or lists as per the user's choice.
# Correctly determine and display whether numbers are even, odd, or prime.
# Implementation Details:
# Use loops to handle lists of numbers.
# Create functions to determine if a number is even, odd, or prime.
# Ensure the program is user-friendly and can handle invalid inputs gracefully.
# Comment on key parts of your code for better readability.

print("Number Classification Program")

#Menu 

print("1. Enter a single digit ")
print("2. Enter a list(0-100) ")

#chossing operations to perfomr 

option=input("Choose option from above ")

evencount,even=0,[]
oddcount,odd=0,[]
primecount,prime=0,[]


if option == "1":
    print("you choose option")
    opt1=int(input("Please write your single number: "))
    
    if opt1 % 2 ==0:     
        evencount += 1
        even.append(opt1)
        print(f"The number {opt1} is even and count is {evencount}")   

    elif opt1 % 1 ==0 and opt1 % opt1 == 0 :  
        for i in range(2, int(opt1 ** 0.5) + 1):
            if opt1 % i == 0:  
             print(f"The number {opt1} is prime and count is {primecount}") 

    elif opt1 % 2 != 0:
        oddcount +=1
        odd.append(opt1)
        print(f"The number {opt1} is odd and count is {oddcount}")   
     
   
        
        
          
        
            
