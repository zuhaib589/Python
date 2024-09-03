# 1st class of oop object oriented programming 

class Car:
    
    def __init__(self,make,model,year): #self represent object and init is constructor it will call automatically 
         print("It is my car")
         self.make=make
         self.modle=model
         self.year=year
         
         
    def display_info(self):
        print(f"This my car company {self.make} and this is model {self.modle} and this is my car year {self.year}")     
        
        
car_one = Car("civic","X","2024")                 
car_one.display_info()         
print()    

# car_two=Car()
# car_two.make="Honda"
# car_two.modle="civic"
# car_two.year="1999"

# car_two.display_info()