# # ---string ---

# # # a= ''' i hope youre doing this for a resaon where we
# # # ash waysdah asdhda '''
# # # print(a)

# # #concationation
# # # a="zuhaib"
# # # b="zafar"
# # # print(a+b)
# # # print(a + " " +b)
# # # print(len(b))


# # # #---string index ---
# # # a="zuhaib"
# # # print(a[2])
# # # print(len(a))
# # # print(a[len(a)-2])


# # #---Slicing String

# a="zuhaib"
# # # # # print(a[0:len(a)-1]) #[start(included) :end(not included) ]
# b=a[len(a)-1] #len(a)=6 [-1]=5 at index 5 "b" is present 
# print(b)
# print(a[-4:-2])

# # #slicing step 

# # # a="zuhaib zafar"
# # # print(a[0:4:2])#[start , end, skip ]

# # # a="hello, world!"
# # # print(a[-9:-5])


# # b="Artificial Intelligence"
# # slice_1=b[: : -1]
# # print(slice_1)


# # c="Artificial Intelligence"
# # # print(c[::3])
# # x="hello world"
# # print(x)

# # print("" .join(x))


# a="hello world"
# print(a.count('l'))
# print(a.endswith("d"))
# print(a.startswith("h"))
# print(a.find("l")) #first occurenece


# #formatting string 
# name="Zuhaib"
# age=20
# f_s=f"My name is {name} and i'm {age} years old"
# print(f_s)

# #replace method .replace("old", "new")
# a="hello, world"
# print(a.replace("world" ,"universe" ).replace())

# #split method
# a="hello, world"
# print(a.split())

#strip whitespaces
# a=" hello, world "
# print(a.strip())
# print(a.lstrip())
# print(a.rstrip())


#reverse method 
# a="hello, world"
# print((reversed(a)))

# _list_=["zuhaib","ammar"]
# a=sorted(_list_) #return new 
# # _list_.sort() #changes original 
# # print(_list_) 
# for i in range(len(_list_)):
#     print(i)
#     z=10
# if z==0:
#     print("hello")
# else:
#     print("no")    


''' 
Reverse and Slice
Question:
Ask the user to enter their name.
Print the name reversed using slicing
Print only the middle 3 characters (assume name is at least 5 characters)

'''
# name=input("Enter Your Name ")
# print(f'Original Name :{name}')
# rev_name=name[::-1]
# print(f'Reversed Name : {rev_name}')
# sli_name=name[2:5]
# print(f'Sliced Name : {sli_name}')

'''
2. Full Name Formatter
Question:
Take input for the first name and last name.
Combine them with a space in between
Print the full name in:
Uppercase
Lowercase
'''
# first_name=input("Enter your firt name : ")
# last_name=input("Enter your last name : ")
# full_name= first_name + " " + last_name
# upper_full_name = full_name.upper()
# lower_full_name = full_name.lower()

# print(f'Full Name is : {full_name}')
# print(f'Full Name in Upper case : {upper_full_name}')
# print(f'Full Name in Lower case : {lower_full_name}')

''' 3. Multiply Lengths of Strings
 Question:
Take two words from the user.
Find the length of both words
Multiply the lengths and print the result
'''
# word1=input("Enter first word : ")
# word2=input("Enter second word : ")
# len_word1=len(word1)
# len_word2=len(word2)
# mul_lengths=len_word1 * len_word2
# print(f'Length of Word 1 is = {len_word1}')
# print(f'Length of Word 2 is = {len_word2}')
# print(f'Length of both words after multiplying = {mul_lengths}')

'''
  4. Simple Slicing Formatter
 Question:
Create a variable msg = "PythonIsAwesome"
Slice and print "Python"
Slice and print "Is"
Slice and print "Awesome."
(Donot ask user input in this one — focus on slicing)
'''

# msg = "PythonIsAwesome"
# slice1=msg[0:6]
# slice2=msg[6:8]
# slice3=msg[8:]
# print(f'Slicing ** {slice1} ** from original string/text')
# print(f'Slicing ** {slice2} ** from original string/text')
# print(f'Slicing ** {slice3} ** from original string/text')

'''
5. Custom Math Expression
Question:
Ask the user to enter three numbers:
Add the first two numbers
Multiply the result by the third number
Print the final result in a formatted message like:
"The final result is: 45"
'''

# num1=int(input("Enter Number 1 : "))
# num2=int(input("Enter Number 2 : "))
# num3=int(input("Enter Number 3 : "))
# sum_1_2=num1 + num2
# print(f'Sum of Number 1 and Number 2 is = {sum_1_2}')
# mul_3= sum_1_2 * num3
# print(f'After multiplying {num3} with sum  {sum_1_2}')
# print(f'The Final Result is = {mul_3}')