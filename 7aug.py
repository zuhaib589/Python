#list recap 
# list1=[1,2,3,5,6,8,9,6,1,1,] 


# print(list1[0])
# print(list1)
# list1[1]="go" # will update the value i index 1 
# print(list1)
# print(list1[-1])
# x=list1[1:4:2] #start: end : gap of 2 mean skip 2 values but 2nd will include and vice versa 
# print(x)

# list1[0:3] = ["list"] # it will change our index value to "list" from 0 to 3 index 
# print(list1)

# 1  will ad element at last 
# list1.append("ali")
# print(list1)

# 2 will add element at specfic index 
# list1.insert(4,"tanzeel")
# print(list1)

# 3 will remove last index elemment 
# list1.pop()
# print(list1)
# and specifc index if given parameter
# list1.pop(1)
# print(list1)

# 4 will remove element of that value
# list1.remove("zuhaib")
# print(list1)

# 9 will clear the list / remove all elements 
# list1=[1,2,3,4]
# list1.clear()
# print(list1)

# will del/remove/pop the specified index value 
# list2 = ["summer", "winter", "spring", "autumn", "sublist"]
# del list2[3] its a keyword not a method
# print(list2)


# 5 will tell index of specific value 
# print(list1.index(1))

# 6 will sort in ascending order 
# list1=["Zuhaib","Hamza", "Ammar" ,"sadia", "ali"]
# list1.sort()
# print(list1)
# will sort and return in reverse order 
# list1.sort(reverse=True)
# print(list1)
# will consider every element as lower chracters
# list1.sort(key=str.lower)
# print(list1) 

# 7 will reverse the order of list
# list1=["Zuhaib","Hamza", "Ammar" ,"sadia", "ali"]
# print(list1)
# list1.reverse()
# print(list1)

# 8 will emerge one list in another list or cancat both list 
# list1=[1,2,3,4]
# list2=["hey", "hi","hello"]
# list2.extend(list1)
# print(list2)
# print(list1 + list2)
 

# 10 will make copy of the list 
# list1=[1,2,3,4]
# copyList=list1.copy()
# print(list1)
# print(copyList)

# 11 will tell how many time elements appear/present in list 
# list1=[1,2,3,4,4,3,4,1,5,6,7,8]
# l=list1.count(4)
# print(l)






























# Tuples
# ordered and unchangeable
# round brackets()

# z=(1) #int
# z=(1,) #tuple
# t=("zuhaib","zafar","hamza")
# print(t[0])
# print(t[-1])
# print(type(t))
# x=t[0:4]
# print(type(x))

