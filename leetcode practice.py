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

a=""
b=""
for i in word1:
    a +=i    
for j in word2 :
    b += j 
print (a ==b)