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

print("1. Add Student Record")
print("2. Update Student Record")
print("3. Delete Student Record")
print("4. View All Student Records")
print("5. Exit")
print()

option=input("Please Choose an option ")

if option != "1" or "2" or "3" or "4" or "5":
  print("Please choose numbers from menu ")

while option =="5":
  print("Exiting the program.Good Bye! ")
  break
# if option == "5":
#   print("Exiting the program.Good Bye! ")
#   # Break()
 
if option == "1":
  print("Please Enter Student Data")     
  print()
  user_name=input("Write student name ")
  user_id=int(input("Write student ID "))
  user_course=(input("Write student Course(sub1,sub2,sub3) ").split(","))
  user_grades=(input("Write student Grades ").upper().split(","))
  
  if len(user_course) > len(user_grades):
      print("you have used more subject than grades ")
  elif len(user_grades) > len(user_course):
    print("you have used more grades than subject")
 

