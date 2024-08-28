# Project Title:Student Management System

# Objective:
# You are tasked with developing a Python-based console application that serves as a comprehensive Student
# Management System. This project will require you to apply all the concepts we have covered throughout
# the course, including data management, control flow, string manipulation, and functions.

# Project Requirements:
# 1. Data Management:
#    - Use dictionaries, lists, tuples, and sets to manage student data, courses, and grades.
# 2. User Interaction:
#    - Create a menu-driven interface for adding, updating, deleting, and viewing student records.
# 3. Control Flow:
#    - Implement loops, conditional statements, and nested loops for smooth program execution.
# 4. String Manipulation:
#    - Ensure proper formatting of student names and information, with search functionality.
# 5. Functions:
#    - Write reusable functions for core tasks, incorporating list comprehensions where necessary.

# Output Example:
# When your program runs, it should look something like this:
# Welcome to the Student Management System
# 1. Add Student Record
# 2. Update Student Record
# 3. Delete Student Record
# 4. View All Student Records
# 5. Exit

# Please select an option: 1
# Enter Student Name: John Doe
# Enter Student ID: 12345
# Enter Courses (comma-separated): Math, Science, History
# Enter Grades (comma-separated, corresponding to courses): A, B, A

# Student Record Added Successfully!
# 1. Add Student Record
# 2. Update Student Record
# 3. Delete Student Record
# 4. View All Student Records
# 5. Exit

# Please select an option: 4
# Student Records:
# 1. Name: John Doe, ID: 12345, Courses: Math, Science, History, Grades: A, B, A
# ```
# Final Deliverable:
# - A fully functional Student Management System.
# - A brief report explaining your code and demonstrating the application of course concepts.



print("Student Management System")
print()

student={}

def add_student():
  
  #adding record 
  
  st_name=input("Write your name: ")
  st_id=input("Write your ID: ")
  st_courses=input("Write your course (comma,seprated): ").split(",")
  st_grades=input("Write your Grades (comma,seprated): ").upper().split(",")
  
  if len(st_grades) != len(st_courses):
   print("The number of grades and course in not equal")
   
    #append/add/pushing record in our dictionary on the basis od Student id (st_id)
    
  student[st_id]={
   "name":st_name,
   "course":[course for course in st_courses],
   "grades":[grades for grades in st_grades]
  } 
  
  print("Record added successfully")
  
def update_student():
  
  st_id=input("Write your ID: ")
  
  if st_id not in student:
    print("There is no student of that ID exist ")
    return
  print(f"Current data for id : {st_id}")
  print(f"Name : {student[st_id]["name"]}")
  print(f"Courses : {",".join(student[st_id]["course"])}")
  print(f"Grades : {",".join(student[st_id]["grades"])}")
  
  
  st_name=input("Enter new name ")
  if st_name:
   student[st_id]["name"]=st_name
  
  st_courses=input("Write your new courses (comma,seprated): ").split(",")
  if st_courses:
    student[st_id["course"]]=[course for course in  st_courses.split(",")]
  
  st_grades=input("Write your new grades (comma,seprated): ").split(",")  
  if st_grades:
    if len(st_grades) != len( student[st_id["course"]]):
      print("The number of new grades must match the number of courses.")
      return
    student[st_id["grades"]]=[grade for grade in st_grades]
    
    
  print("student record updated ")
  
  
    
    
      
  
  



while True:
  print("1. Add Student Record ")
  print("2. Update Student Record ")
  print("3. Delete Student Record ")
  print("4. View All Student Records ")
  print("5. Exit")
  print()
    
  option=input("Choose from option ")
  if option == '1':
            add_student()
  elif option == '2':
            update_student()
  elif option == '3':
            pass
  elif option == '4':
            pass  
  elif option == '5':
     print("Exiting the program. Goodbye!")
     break
  else:
    print("Invalid option. Please try again.")  
