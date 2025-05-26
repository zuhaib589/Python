# a=int(input("Enter 1st number "))
# b=int(input("Enter 2st number "))
# c=int(input("Enter 3st number "))

# if a >b and a > c:
#     print(f'{a} is greater than {b} and {c} ')
# elif b> a and b>c :    
#         print(f'{b} is greater than {a} and {c} ')
# else:
#      print(f'{c} is greater than {a} and {b} ')

# edx=1
# ebx=100
# count=0
# while edx < ebx:
#     edx += 1
#     count +=1
# print(count)    


# a=[1,2]
# b=a
# a[0]=99
# print(a)
# print(b)
# b.pop()
# print(b)
# print(a)  

# from AI import call_gpt 
# country=input("Country :")
# response=call_gpt(f"what is the capital of {country}")
# print(response)


'''Even or Odd Counter in a Range
💡 Overview
The program:
Asks the user for a starting and ending number.
Goes through each number in that range.
Counts how many are even and how many are odd.
Displays the results.
✅ Covers
✅ Python syntax
✅ Variables
✅ Operators (%, +)
✅ Conditions (if)
✅ Loops (for)
'''

Starting_number = int(input("Enter Starting Number: "))
Ending_number =   int(input("Enter Ending Number: "))
even=0
odd=0
for i in range(Starting_number,Ending_number+1):
    if i % 2 == 0 :
        even +=1
    else:
        odd +=1
        
print(f'Total even number from {Starting_number} to {Ending_number} are : {even}')        
print(f'Total odd number from {Starting_number} to {Ending_number} are : {odd}')        