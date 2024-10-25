# ##dictionary in python          

# #how to create dictionary 

# # person ={
# #     "Name":"Zuhaib",
# #     "Age" :20 ,
# #     "City":"Faisalabad",
# #     "Email":"zuhaibzafar589@gmail.com"
# # }

# #printing full dictionary

# # print(person)

# # Accessign Single Elements in dictionary
# # print(person["Age"])
# # 
# #Adding Elements in Dictionary
# # person["Last_Name"] ="Zafar"

# # print(person)

# #Changing Value in dictinary
# #remember KEY can't be duplicate in Dictionary vice versa (Value can be )


# # person["Name"] ="Ammar"

# # print(person)


# #Nested Dictionary 

# person ={
#     "Name":"Zuhaib",
#     "Age" :20 ,
#     "City":"Faisalabad",
#     "Email":"zuhaibzafar589@gmail.com",
#     "location":{
#         "city": "Faisalabad",
#         "state": "Punjab"
#     }
# }
# # print(person['location']["city"]) #Faisalabad

# #using loop 

# for i in person :
#  print(i, person[i])
# #  if( type(person[i])== type({})) :
# #   for j in person[i]:
# #    print(j,person[i][j]) 


student={
    "name":"zuhaib zafar",
    "roll-no":"FC-204",
    "class":"BSCS 5TH ",
    "Age":20,
    "uni":"National university of modern language",    
}

# print(student['name'])

# copyList=student.copy()

# print(copyList)

# copyList.clear()

# print(copyList)

# x=["key1","key2","key3"]
# y=["val1","val2","val3"]
# td=dict.fromkeys(x,y) #it will take 1st argu as keys and 2nd argu as value for every key there will be all values as in 2nd argu
# print(td) #E.g key1["val1","val2","val3"]

# print(student.get("Age",30)) #specific value as per given key 

# print(student.items()) #will return tuple for every key-value pair 

# print(student.keys()) #will return all keys in dict

# print(student.pop("name")) #will remove given value

# # print(student["name"]) # will give error as we have poped it 

# print(student.popitem()) # will pop last key-value pair 

x=student.setdefault("Age","21") # ans 20 will set default value of key if not given else it will add new pair 
print(x)
# x=student.setdefault("Name","zuhaib zafar") #add name and zuhaib as key value will set default value of key if not given else it will add new pair 
# print(x)

# y=student.update({"subject":"6"}) # will add new pair

# y=student.update({"class":"BSCS 6TH"}) # key-value update existing 

# print(student)

# print(student.values()) #will print all values 

# del student["roll-no"]

# print(student)

# for i in student:
#     print(f"your {i} is {student[i]}") # i will print key and student[i] will print values
    
    
#     #Adding two dictionary 
# teacher={
#     "t_name":"Asma",
#     "subject":"Database"
# }    
# student.update(teacher)
# print(student)

# x=student | teacher
# print(x)

# print(student)