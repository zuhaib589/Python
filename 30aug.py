# reverse a integer using while loop 

def reverse_number(num):
    
    reversed=0
    while num >0:
        reversed=reversed*0 + num %10
        num //= 10
    return reversed    
        
reverse_number(123)        


