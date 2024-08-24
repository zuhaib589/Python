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

while True:
  print("1. Add Student Record")
  print("2. Update Student Record")
  print("3. Delete Student Record")
  print("4. View All Student Records")
  print("5. Exit")
  print()
    
  option=input("Choose from option ")
  if option == '1':
            pass
  elif option == '2':
            pass
  elif option == '3':
            pass
  elif option == '4':
            pass  
  elif option == '5':
     print("Exiting the program. Goodbye!")
     break
  else:
    print("Invalid option. Please try again.")  
