# reverse a integer using while loop 

def reverse_number(num):
    
    reversed=0
    while num > 0:
        reversed=reversed*num + num % 10
        num //= 10
    return reversed    
        
print(reverse_number(123))


# Problem 15: Write a program that prints the multiplication table of a given number using a for loop.

def table(num):
    a=11
    for i in range(1,a):
     print(f" {num} x {i} = {num*i}")   
     
        
table(2)
table(-3) 
     
# 18: Write a program using a for loop to calculate the factorial of a given number.


def factorial(n):       
    ans=1
    for i in range(1,n+1):
        ans *= i
        
    return ans 

factorial(4)     



# Problem 16: Create a program that uses a while loop to find the sum of digits of a given positive integer.

def sumofdigit(n):
    
    if n < 0 :
     return print("Sorry digit cannot be negative integer  ")

    total=0
    while n > 0:
       total= total + n % 10     
       n=n//10
    print(total)    
      
      
        
sumofdigit(18)      