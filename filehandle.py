employee_file = open("employees.txt", "r") # "w" for write, "a" for append, "r+" both read and write

print(employee_file.readable()) # readable tell if readable or not
#print(employee_file.read())  # or readline() only specfic line
print(employee_file.readlines()) # print(employee_file.readlines()[1]) for specfic number
employee_file.close()

#Writing new files
employee_file = open("employees1.txt", "a")
employee_file.write("\neminem - customer service") #\n for adding into new line