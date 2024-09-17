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

print("123")