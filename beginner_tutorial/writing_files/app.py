# writing files 

# r - read, w - write (rewrites the entire file!), r+ read/write, a append

employee_file = open("C:/Users/leffg_54lmf5u/OneDrive/Documents/CODE/SNAKE/python_projects/python_projects/beginner_tutorial/writing_files/employees.txt" , "a") # append to the file

employee_file.write("Toby - Human Resources\n") # be cautious of appending!

employee_file.close()

index_file = open("index.html", "w")

index_file.write("<p>This is HTML</p>")

index_file.close()