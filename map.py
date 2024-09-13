# # map function 


# def squared_number(num):
#     return num **2


# li=[1,2,3,4,5]
# maps=set(map(squared_number,li))
# print(maps)




# def even(n):
#     return n % 2 == 0
    
# lst=[1,2,3,4,5,6,7]    
# filters=list(filter(even,lst))    
# print(filters)



# with lamda function 

l2=[1,2,3,4,5,6,7,8,9,10]
lam=list(filter(lambda i :i >5 or i %2 ==0,l2))
print(lam)