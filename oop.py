# # # 1st class of oop object oriented programming 

# # class Car:
    
# #     def __init__(self,make,model,year): #self represent object and init is constructor it will call automatically 
# #          print("It is my car")
# #          self.make=make
# #          self.modle=model
# #          self.year=year
         
         
# #     def display_info(self):
# #         print(f"This my car company {self.make} and this is model {self.modle} and this is my car year {self.year}")     
        
        
# # car_one = Car("civic","X","2024")                 
# # car_two = Car("civic","X","2026")                 
# # car_one.display_info()         
# # print()    

# # # car_two=Car()
# # car_two.make="Honda"
# # car_two.modle="civic"
# # car_two.year="1999"

# # car_two.display_info()



# # inheritance
# # 1-parent-> child 
# # 2-parent-> child -> child(sub child of parent)
# # 3- parent -> child1 -> child2


# # # Base class
# # class BaseClass:
# #     def __init__(self):
# #         self.attribute1 = "Attribute 1"
# #         self.attribute2 = "Attribute 2"

# # # Child class
# # class ChildClass(BaseClass):
# #     def __init__(self):
# #         super().__init__()  # Initialize the base class attributes
# #         self.child_attribute = self.attribute1  # Use only attribute1

# #     def show_attribute(self):
# #         print(f"Using {self.child_attribute} in ChildClass")

# # # Create an instance of the ChildClass
# # child = ChildClass()
# # child.show_attribute()


# # to not use all attriubutes from parent when calling(inhereting) we pass none keyword




# # transitive nature of inheritance 

# class Parent:
    
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
        
        
#     def family(self):    
#         print(f'My name is {self.name} and i am {self.age} years old')
        

# class child1(Parent):
    
#     def __init(self,none,name,age,run):
#         self.run=run
#         super().__init__(age)
#         print(f'{name,age}')
        
        
        
        
        
# zuhaib=Parent("zuhaib",20)
# zuhaib.family()

# hamza=child1("Hamza",)
# hamza.family()
# # print(hamza.__dict__)
    
# # zuhaib.__init__("hamzaali",40)          
         
# # iterator in Python
# # it is like and object that contains a countable number of values 

# # iter and next 

# a=[1,2,3]
# b=[4,5,6]
# for i in (a,b):
#     print(a,b)


class car:
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
        
    def move(self):
        print("drive")  
 
class boat:
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
        
    def move(self):
        print("sail")   
                  
    def movee(self):
        print("gggl")             
        
        
car1=car("honda","X")        
BOAT1=boat("pak","XX")        
        
for x in (car1,BOAT1):
    x.move()   
    # x.movee()        

        
        
        
