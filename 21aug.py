# foor loop 
# list=["a","b","c"]
# for i in list:
#     print(i)



# range fucntion/method in for loop 
# used to get index and value as we
# ll 

# list=["a","b","c"]
# for i in range(len(list)):
#     print(i, list[i])

list=["b","c","a","z","g"]
target="a"
for i in list:
    if i == target:
        print("found")
        continue
    else:   
        print("not found")


# functions

def sum(a,b):
    return a+b

print(sum(2,2))

     