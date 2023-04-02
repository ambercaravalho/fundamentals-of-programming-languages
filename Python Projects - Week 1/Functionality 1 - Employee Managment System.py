# Coded by Amber Caravalho for the University of Arizona Global Campus
# CPT 200: Fundamentals of Programming Languages//Dr. Amr Elchouemi
# Functionality 1 - Employee Management System

# Formats and centers the introduction statement, then prints it to the screen
print (" "); introduction = "Welcome to the Employee Management System!"
introduction = introduction.center(50)
print (introduction)

# Requests user input, then stores them as string variables
employeeName = input ("Employee's Name: ")
employeeSSN = input ("Employee's Social Security Number: ")
employeePhone = input ("Employee's Phone Number: ")
employeeEmail = input ("Employee's Email Address: ")
employeeSalary = input ("Employee's Salary: $")

# Formats and centers the employee's name, then prints it to the screen
employeeNameBanner = '{:-^38}'.format(employeeName)
employeeNameBanner = employeeNameBanner.center(50)
print (" "); print (employeeNameBanner)

# Prints remaining formatted employee data to screen
print ("SSN:", employeeSSN)
print ("Phone:", employeePhone)
print ("Email:", employeeEmail) 
print (f"Salary: ${employeeSalary}")

# Centers the banner at the bottom of the employee data output
lowerBanner = "---------------------------------------"
lowerBanner = lowerBanner.center(50)
print (lowerBanner); print (" ")

# Prevents the Python output window from closing until the enter key is pressed
input("Press enter to exit.")