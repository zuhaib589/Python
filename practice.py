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

#  12: Create a function that takes a tuple and an element,
# and returns a new tuple with the element added to the end of the tuple.


def tupl_plus_ele(tup,ele):
    print (tup + ele)
    
    
t1=(1,2,3,4)
ele=6,  
tupl_plus_ele(t1,ele)   



#  6: Write a program that takes a list of integers and returns the list sorted in ascending order.

l1=[1,2,4,6,5,3,0,-1]

def sort_list(n):
    n.sort()
    return n
    
  
print(sort_list(l1) )
    
    
#7:Create a program that takes a list and a number n, and returns a new list with the first n elements removed.

list1=[1,2,3,4,5,6,7,8,9,10]

def removeing_from_list(list1,n):
   return list1[n:]

n=4    

print(removeing_from_list(list1,n))


#Problem 8: Write a function that takes two lists and returns a list containing only the elements that are common to both lists.

def  common_elements(l1,l2):
    l3=[]
    for i in range(len(l1)):
        if l1[i] in l2:
            l3.append(l1[i])
    return l3       

    
    
    
 
l1=[1,2,3,4,5,6,7,8,9]
l2=[2,3,4,5,6]
# common_elements(l1,l2)
print(common_elements(l1,l2))