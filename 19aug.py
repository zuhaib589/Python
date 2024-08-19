#shorthand if else 
a=5
b=5
print("a") if a>b else print("b")
print("a") if a<b else print("same") if a==b else print("hello")


#logical operators in conditions

a = 50
b = 100
c = 300
if a>b or a>c:
  print("a is greater than all")
elif b>a or b>c:
  print("b is greater than all")
elif c>a and c>b:
  print("c is greater than all")

# pass keyword
# when we don;t wnat to run our if condition if it is true 

a=5
b=19
if  a<b:
    pass
else:
    print("Fail")
