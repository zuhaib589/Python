# Problem Statement:
# You are tasked with designing a system for managing various types of employees in a company. Different types of employees share some common attributes and methods, but also have their own unique characteristics. To avoid rewriting code, you will use inheritance to model this system.

# Task:
# Create a Base Class Employee:
# The Employee class should have the following attributes:

# name (e.g., "John Doe")

# employee_id (e.g., "E12345")

# The Employee class should also have a method called display_details that prints the employee's name and employee ID.

# Create a Child Class Manager:
# The Manager class should inherit from the Employee class.

# In addition to the attributes inherited from Employee, the Manager class should have an additional attribute department (e.g., "Sales").

# The Manager class should override the display_details method to include the department information in the output.

# Create Objects:
# Create an object of the Employee class and an object of the Manager class. Call the display_details method for both objects to show how the Manager class reuses and extends the attributes and methods of the Employee class.

class Employee:
  def __init__(self,name,employee_id):
    self.name=name
    self.employee_id=employee_id


  def details(self):
    print(f'Employee Name : {self.name}')  
    print(f'Employee ID : {self.employee_id}')  

class Manager(Employee):

  def __init__(self,name,employee_id,department):
    super().__init__(name,employee_id)
    self.department=department

  def details(self):
    print(f'Department : {self.department}')
    
    
  def detail1(self):
    super().details()
    print(f'Department dasd: {self.department}')  


employee=Employee("Zuhaib",124)
employee.details()
# employee.details1()

print("\n")

manager=Manager("Zafar",124,"Computer Scienece")
manager.details()