#Python Syntax and Basic Concepts 

# question1. Write a Python script that prints "Hello, World!" to the console.
# print("Hello, World!"")

#Question 2. Add  single line comments to the script from Question 1 explaining what each line does. 
#Ans: For single line comment we use "#" before the line  in python
# a="Hello, World!"

#Question 3 Add Multiline comment and repeat question no 2 
#Ans: for multi line comment we use tripple(3x) inverted commas

''' a=" hello world  "
print(a)  '''


                                 #Pythone Variables

#4. Create a variable named `name` and assign it your name. Print the variable.

# name="Zuhaib Zafar"
# print(name)

#5. Create variables `x`, `y`, and `z`, and assign them the values 10, 20, and 30, respectively. 
#Print their values in a single line. 

# x=10
# y=20
# z=30
# print(x,y,z)


#6Assign the value` 100' to three different variables (`a`, `b`, and `c`) in one line of code.Print each variable
# a=b=c=100
# print("a=",a  , "b=", b , "c=", c)

#7Write a script to get and print the memory address of the variable `x` from Question 5.
# print("Address of x is ",id(x))

#8.Write about 10 possible variable names, including multi-word names and names with 
#numbers.Ensure the variable names follow Python naming conventions. Assign different data 
#types to each of these variables and print their types.

'''ans:3 cases used in python 
Camel Case => theCamelCase
Snake Case => the_snake_case
Pascal Case => PascalCase
''' 
# theCamelCase=10
# the_snake_case=20
# PascalCase=30
# name="Zuhaib"
# Name="Ali"
# Age=20 
# age=21
# the_10=12
# x="hamza"
# y="Aaliyah"
# print(the_snake_case,the_snake_case,age,Age,name,Name,the_10,PascalCase,x,y)


                   #Data Types and TypeCasting


#9. Create a variable with an integer value and convert it to a float. Print the result.

# a=20
# print(a)
# print("After convertiong in float = ", float(a))

#10. Create a variable with a string value representing a number, convert it to an integer, and print

# a="10"
# print(a)
# print("After convertiong in integer = ", int(a))

#11.Print the data type of the variable `age`. Type cast the variable `age` to a float data type and print 

# Age=29
# print(type(Age),Age) #int
# convert_float=float(Age)
# print(type(convert_float),convert_float) #float
# convert_string=str(convert_float)
# print(type(convert_string),convert_string)
# concat="hey i'm zuhaib "
# if convert_float > 30 :
#  print(concat + convert_string)


                               #Operators

#12. Write a script that calculates and prints the result of the expression `5 + 10 * 2`.

# result = 5 + 10 * 2
# print("The result of the expression 5 + 10 * 2 is:", result)

#13. Write a script that assigns the value `15` to a variable `num`, then uses the addition 
#assignment operator to add `10` to `num`. Print the result.

# num=15
# num += 10
# print(num)

#14. Write a script that creates two variables with the same value and checks if they are the 
#same object in memory using identity operators. Print the result. 

# a=b=20
# print(id(a))
# print(id(b))


                                        #Python Strings
# 15.  
# x = 42 
# y = "hello" 
# z = [1, 2, 3] 
# a = 3.14 
# b = False 
 
# # Assignments and operations 
# x = y 
# y = z[1] 
# z[2] = x 
# a = b 
# b = x == y 
# 1. What are the resulting values of x, y, z, a, and b after all the assignments and operations? 
# 2. What are the resulting data types of x, y, z, a, and b after all the assignments and operations?     
# answers
                                    
# x=42 then x=y which means x=hello as y is equal to hello  
#y is equal to hello and then y=z[1] which means the value from 1st index in z will store in y which is 2  
#z is list with values [1,2,3] and then z[2]=x which means x value will be stored in index 2 so z=[1,2,hello]
#a=3.14 float value then a=b which means b value will be store in a which false 
#b=false and then b = x == y which means if x==y it will give false as x is equal to hello and y equal to 2

# print(type(x),x) # hello type string 
# print(type(y),y) # 2 type int
# print(type(z),z) # [1,2,hello] type list
# print(type(a),a) # False type bool 
# print(type(b),b) #false type bool 

#16.You are Given an unknown  string you dont what is written in the string you have to write the 
# second last character  of string Explain how you will do this is comment

# a=input("Write a Your Name ")
# if len(a) >= 2 :
#      print(a[-2])
# else:
#      print("string is too short to access 2nd last element")


#17. Create a multiline string and print it.

# string_multiline=""" Hi I'm Zuhaib Zafar 
# and I'm learning Python from
# icodeguru at 11pm session  
# """
# print(string_multiline)

#18. Concatenate two strings and print the result.

# str1="Hello"
# str2="I'm Zuhaib"
# print(str1+ " " +str2)

#19. Write a script to find and print the length of a string.

# Name=input("Write your name ")
# print(len(Name))

#20. Create a string variable and print the character at the index position `2`.

# string_variable="Hello Wordl!"
# print(string_variable[2])

#21. Write a script that takes a string and prints it in reverse order.

# original_string = input("Enter a string: ")
# reversed_string = original_string[::-1]
# print("The reversed string is:", reversed_string)

