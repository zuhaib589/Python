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

# # # a="zuhaib"
# # # # print(a[0:len(a)-1]) #[start(included) :end(not included) ]
# # # # b=a[len(a)-1] #len(a)=6 [-1]=5 at index 5 "b" is present 
# # # # print(b)
# # # print(a[-4:2])

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
a="hello, world"
print((reversed(a)))