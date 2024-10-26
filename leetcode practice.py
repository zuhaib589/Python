# nums = [0,2,1,5,3,4,]
# # nums.sort()
# # print(nums)
# ans=[]
# for i in range(len(nums)):
# #  x=[i,nums[i]]
#  print(i,nums[i])
# #  desired_ans=nums[x]
# #  print(desired_ans)


# nums = [0,2,1,5,3,4]
# a=nums.copy()
# ans=a+nums
# print(ans)
# for i in nums:
# #  print(i,nums[i])
#  print(nums.index(i))

# 1464. Maximum Product of Two Elements in an Array


#  greatest = max(nums)
#nums.remove(greatest)
#greater2 = max(nums)
#product = (greatest-1)* (greater2 - 1)
#return product

# nums = [0,1,0,3,12]
# arr=[]
# arr1=[]
# for i in range(len(nums)):
#     if nums[i] == 0:
#      arr.append(nums[i])
#     else:
#      arr1.append(nums[i])
# print (arr1 + arr)


# 1662:
# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

# word1 = ["ab", "c"]
# word2 = ["a", "bc"]
# a=""
# b=""
# for i in word1:
#     if i not in a:
#         a +=i

# for j in word2 :
#    if j not in b:
#        b += j 
# print(a == b )
# print(a ,b )

# sol 2 

# a=""
# b=""
# for i in word1:
#     a +=i    
# for j in word2 :
#     b += j 
# print (a==b)


# https://leetcode.com/problems/find-the-difference-of-two-arrays/
# 2215
# class Solution:
#     def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
#             ans1=[]
#             ans2=[]
#             main=[]
#             for i in range(len(nums1)):
#                 if nums1[i] not in nums2 and nums1[i] not in ans1:
#                     ans1.append(nums1[i])
#             main.append(ans1)
#             # print(main)
#             for j in range(len(nums2)):
#                 if nums2[j] not in nums1 and nums2[j] not in ans2:
#                     ans2.append(nums2[j])
#             main.append(ans2)
#             return main

# sol 2

# set1 = set(nums1)
# set2 = set(nums2)
    
#     # Find the difference between the sets
# diff1 = list(set1 - set2)  # Elements in nums1 but not in nums2
# diff2 = list(set2 - set1)  # Elements in nums2 but not in nums1
    
#     # Return the result as a list of two lists
# print( [diff1, diff2])

# print("123")


# Q: Ask the user to enter three numbers. Add together the first two numbers and then multiply this total by the third. Display the answer as The answer is [answer].

# num1=int(input("Enter 1st number "))
# num2=int(input("Enter 2nd number "))
# num3=int(input("Enter 3rd number "))

# answer=(num1+num2)*num3
# print(f'Answer is {answer}')

# Q: Ask the user for their name and their age. Add 1 to their age and display the output [Name] next birthday you will be [new age].

""" name=input("Enter your name ")
age=int(input("Enter your age "))
print(f"{name} next birthday you will be {age+1} ") """

# Q:Ask the user to enter their first name and surname is lower case. Change the case to title case and join them together. Display the finished result.

""" f_name=input("Enter first name ").lower()
    l_name=input("Enter last name ").lower()
    print(f_name.title() + " " + l_name.title()) """
    
#  Q:Ask the user to type in the first line of a nursery rhyme and display the length of the string. Ask for a string number and an ending number and then display just that section of the text (remember Python starts counting from 0 and not 1).

text=input("Enter Nursery Rhyme: ")
len_text=len(text)
print(f"Lenght of string is {len_text}")
print()
print("Write starting and ending number to see subtext from original (index base remember it starts from 0 ) ")

s_num=int(input("Enter starting number: " ))
e_num=int(input("Enter ending number: " ))

print(text[s_num:e_num])

   

