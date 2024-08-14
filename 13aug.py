# SETS
# unordered,unmuteable,no indexing.don't allow duplicates 

# set1={"zuhaib",7,3,4,True,False,'hello',7.0} #True or 1 , False or 0 
# print(len(set1))
# print(type(set1))

# Access items 

# if "zuhaib" in set1:
#  print(True)

#  print("zuhaib" in set1)

#  Add in Sets add method 
# set1.add("zafar")
# print(set1)
# print(len(set1))

#to add set1 in set2 or update value 
# set2={1,2,4,5,"hell0"}
# set3={12,13,15,"zuhaib"}
# set4= set2 + set3 #will not work
# print(set4) 
# set2.update(set3)
# print(set2)
# set2.update("qasim ")
# print(set2)




# remove items in sets
# set2={1,2,4,5,"hell0"}
# set2.remove(1) #If we give any item that is not in set it will give error
# print(set2)
# set2.discard("he00") #If we give any item that is not in set it will not give error
# print(set2)



#clear and del 
# set2={1,2,4,5,"hell0"}
# set2.clear() #will remove all items 
# print(set2)
# del set2
# print(set2) #will del full set nothing to show


#join sets intersection and union |(pip sign) operator
# set2={1,2,4,5,"hell0"}
# set3={"zuhaib",2,3,4}
# uni=set2.union(set3) #or set2|set3
# print(uni)

# inter=set2.intersection(set3)
# print(inter)


# some set methods

# intersection_update will update first set and reutrn new values

# set2={1,2,4,5,"hell0"}
# set3={"zuhaib",2,3,4} 
# set2.intersection_update(set3)
# print(set2)

# intersection will return us new set 
# set2={1,2,4,5,"hell0"}
# set3={"zuhaib",2,3,4}
# uni=set2.union(set3) #or set2|set3
# print(uni)

# difference 
# in first set but not in second
# set2={1,2,4,5,"hell0"}
# set3={"zuhaib",2,3,4}
# x=set2.difference(set3)
# print(x)

# symmetric difference 
# will return uncommon in boths

# set2={1,2,4,5,"hell0"}
# set3={"zuhaib",2,3,4}
# x=set2.symmetric_difference(set3)
# print(x)

