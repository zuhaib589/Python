''' 1. Grading System:
   Create a program that asks the user to input their marks. Based on the marks entered,
    the program should assign and display the appropriate grade.'''

marks=float(input("Enter your Marks "))

if marks < 0 or marks > 100:
   print("Please write correct number (0-100)") 

elif marks >= 90 and marks <= 100:
    print("You got A+")    

elif marks >=80 and marks <90:    
    print("You got A") 

elif marks >=70 and marks <80:    
    print("You got B") 

elif marks >=60 and marks <70:    
    print("You got C")  

elif marks >=50 and marks <60:    
    print("You got D")  

else:    
    print("You got F")   




''' 2. Simple Calculator: 
   Develop a simple calculator program. The program should:
    Ask the user to input two values.
    Ask the user to choose an operation (e.g., addition, subtraction, multiplication, or division).
    Perform the selected operation and display the result.'''

# Num1=float(input("Number 1 = "))
# Num2=float(input("Number 2 = "))
# operation=input("Choose operation: mul, add, sub, div ::")

# if  operation == 'mul':
#    result=Num1*Num2 
#    print(result)
# elif  operation == 'add':
#    result=Num1 + Num2 
#    print(result)
# elif  operation == 'sub':
#    result=Num1 - Num2 
#    print(result) 
# elif  operation == 'div':
#       if Num2 != 0:
#        result= Num1 / Num2 
#        print(result) 
#       else:
#          print("error!! Num 2 cannot be = 0")
# else :   
#    print("Please Choose valid operation ")

