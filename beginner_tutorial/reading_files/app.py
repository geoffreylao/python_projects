# reading files 

# r - read, w - write, r+ read/write

employee_file = open("C:/Users/leffg_54lmf5u/OneDrive/Documents/CODE/SNAKE/python_projects/python_projects/beginner_tutorial/reading_files/employees.txt" , "r") # read the file

print(employee_file.readable()) # boolean to see if file is readable

for employee in employee_file.readlines():
    print(employee)

employee_file.close()