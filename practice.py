# List and tuples examples for pracitce

# Problem 11: Write a program that takes a tuple of numbers and returns a tuple with each number squared.

def squared_tuple(n):
    
    t1=()
    for i in n:
     l1=list(t1)
     l1.append(i*i)
     t1=tuple(l1)   
    print(t1)
        

num=(1,2,3,4,5,6,7,8,9)
squared_tuple(num)