# Assignment: Practice with Logical Operators in Conditions



# 1. Question 1: Write a program that accepts a user’s age, citizenship status, and criminal 
# record status. Determine if the user is eligible to vote. A person is eligible to vote
# if they are at least 18 years old, are a citizen of the country, and do not have a criminal
# record. Use logical operators to check all these conditions in a single statement.

'''Age=int(input("Write your age: "))
Country=input("Write you country: ")
C_Record=input("Do you have criminal record ? (yes / no): ")

print("You're eligible to vote") if Age >= 18 and Country =="pakistan" and C_Record == "no" else print("You can't vote")'''
  
 
# 2. Question 2: Create a program that takes three integers as input and determines whether 
# they can form an arithmetic progression. The numbers form an arithmetic progression if 
# the difference between consecutive numbers is the same. Use logical operators to validate
# this condition and print whether the numbers form a valid sequence.  

""" num1=int(input("Enter number 1 "))
num2=int(input("Enter number 2 "))
num3=int(input("Enter number 3 "))

if num2-num1 == num3-num2: 
    print("numbers form an arithmetic progression")
else:
    print("numbers doesnot form an arithmetic progression") """
    
    
#  3. Question 3: Write a program that checks if a given year is a leap year. A year is a leap year
#  if it is divisible by 4, but not divisible by 100 unless it is also divisible by 400. Use nested
#  logical operators to make this determination in a single conditional statement.   



''' year=int(input("Enter year"))

if  (year % 4 ==0 and year % 100 !=0 ) or  year % 400 ==0  :
 print(year,"is a leap year")
else:
 print(year,"is not leap year") '''
 
 
 
# Question 4: Develop a program that takes a students grades in three subjects as input.Determine 
# if the student has passed or failed based on the following criteria: the student must have a grade of at 
# least 50 in each subject, and the average grade must be 60 or above. Use logical operators to evaluate 
# these conditions and print the result.

sub1=int(input("Write number of subject 1 "))
sub2=int(input("Write number of subject 2 "))
sub3=int(input("Write number of subject 3 "))

