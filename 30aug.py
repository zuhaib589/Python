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
     print(f" {num} x {i} ={num*i}")   
        
        
      
        
table(2)
table(-3)