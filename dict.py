##dictionary in python          


#how to create dictionary 

# person ={
#     "Name":"Zuhaib",
#     "Age" :20 ,
#     "City":"Faisalabad",
#     "Email":"zuhaibzafar589@gmail.com"
# }

#printing full dictionary

# print(person)

# Accessign Single Elements in dictionary
# print(person["Age"])
# 
#Adding Elements in Dictionary
# person["Last_Name"] ="Zafar"

# print(person)

#Changing Value in dictinary
#remember KEY can't be duplicate in Dictionary vice versa (Value can be )


# person["Name"] ="Ammar"

# print(person)


#Nested Dictionary 

person ={
    "Name":"Zuhaib",
    "Age" :20 ,
    "City":"Faisalabad",
    "Email":"zuhaibzafar589@gmail.com",
    "location":{
        "city": "Faisalabad",
        "state": "Punjab"
    }
}
# print(person['location']["city"]) #Faisalabad

#using loop 

for i in person :
 print(i, person[i])
 if( type(person[i])== type({})) :
  for j in person[i]:
   print(j,person[i][j]) 
