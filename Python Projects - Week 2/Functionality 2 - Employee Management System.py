# Coded by Amber Caravalho for the University of Arizona Global Campus
# CPT 200: Fundamentals of Programming Languages//Dr. Amr Elchouemi
# Functionality 2 - Employee Management System


# Creates the dictionary and variables required for data storage later
masterEmployeeData = {}
entryCounter = 1
addAnotherEntry = "y"
firstRun = "y"


# Prints the line and welcome statement
line = "---------------------------------------------------"
print(line)
print ("Welcome to the Employee Management System!")


def mainProgram():
    # Makes addAnotherEntry a global variable so it can be accessed by this function
    global addAnotherEntry


    def requestUserInput():
        # Makes entryCounter a global variable so it can be accessed by this function
        global entryCounter

        # Prints the current employee's number to the screen
        print(f"\nPlease enter the information for employee {entryCounter} below:")

        # Requests user input, then stores them in the list created earlier
        masterEmployeeData[entryCounter] = ([input("Employee's Name: "), 
        input("Employee's Social Security Number: "), input("Employee's Phone Number: "), 
        input("Employee's Email Address: "), input("Employee's Salary: $")])

        # Advances the masterEmployeeData dictionary key value each time the script is run
        entryCounter = entryCounter + 1


    def addEmployeeData():
        # Makes addAnotherEntry a global variable so it can be accessed by this function
        global addAnotherEntry

        while addAnotherEntry == "y" and entryCounter != 6:
            # Calls the requestUserInput function
            requestUserInput()
            
            # Asks the user if they want to enter another employee's information
            addAnotherEntry = input("\nWould you like to add another entry to the system? (Y/N): ").lower()


    # Calls the addEmployeeData function to request user input
    addEmployeeData()


    while addAnotherEntry != "n":
        # Tells the user that they need to type y or n only.
        addAnotherEntry = input("Non-valid input, please type Y or N: ").lower()

        # Calls the addEmployeeData function to request user input again
        addEmployeeData()
        

    def lookupEmployee():    
        # Makes firstRun, lookup, and addAnotherEntry global variables so they can be accessed by this function
        global firstRun
        global lookup
        global addAnotherEntry

        # Resets the addAnotherEntry variable to "y"
        addAnotherEntry = "y"

        while firstRun == "y":
            # Asks the user which employee they want to search for
            lookup = str(input("\nType a number to look up an employee: "))

            # Ensures that this question only display the first time the application is run
            firstRun = "n"

        # Makes sure the user input is a number, then converts it to an integer
        if lookup.isnumeric() == True:
            lookup = int(lookup)

            if lookup in masterEmployeeData:
                # Converts the user input list to a string, then prints it to the screen
                print(f"\n{line}")
                print(",".join(masterEmployeeData[lookup]))
                print(line)
            
            else:
                # Prompts the user to type a valid number
                lookup = str(input("Non-valid input, please type a number between 1 and 5 only: "))

                # Calls the lookupEmployee function to request user input again
                lookupEmployee()
        
        else:
            # Prompts the user to type a valid number
            lookup = str(input("Non-valid input, please type a number between 1 and 5 only: "))

            # Calls the lookupEmployee function to request user input again
            lookupEmployee()


    # Calls the lookupEmployee function to request user input
    lookupEmployee()


    # Asks the user if they want to look up another employee's information
    addAnotherEntry = input("\nWould you like to look up another employee? (Y/N): ").lower()
    

    def lookupMore():
        # Makes firstRun and addAnotherEntry global variables so they can be accessed by this function
        global addAnotherEntry
        global firstRun

        while addAnotherEntry == "y":
            # Resets the firstRun variable to "y"
            firstRun = "y"
            
            # Calls the addEmployeeData function to request user input again
            lookupEmployee()

            # Asks the user if they want to look up another employee's information
            addAnotherEntry = input("\nWould you like to look up another employee? (Y/N): ").lower()

        while addAnotherEntry != "n":
            # Tells the user that they need to type y or n only.
            addAnotherEntry = input("Non-valid input, please type Y or N: ").lower()

            # Calls the addEmployeeData function to request user input again
            lookupMore()

    # Calls the lookupMore function to request user input    
    lookupMore()


# Calls the mainProgram function to display the initial application
mainProgram()


# Asks the user if they want to enter another employee's information
addAnotherEntry = input("Would you like to add another entry to the system? (Y/N): ").lower()


def lastMinuteAdditions():
    # Makes firstRun and addAnotherEntry global variables so they can be accessed by this function
    global addAnotherEntry
    global firstRun

    # Resets the firstRun varaible to "y"
    firstRun = "y"

    while addAnotherEntry == "y" and entryCounter != 6:
        # Calls the mainProgram function
        mainProgram()

        # Asks the user if they want to enter another employee's information
        addAnotherEntry = input("Would you like to add another entry to the system? (Y/N): ").lower()


# Calls the lastMinuteAdditions function to request user input 
lastMinuteAdditions()


while addAnotherEntry != "n":
    # Tells the user that they need to type y or n only.
    addAnotherEntry = input("Non-valid input, please type Y or N: ").lower()

    # Calls the addEmployeeData function to request user input again
    lastMinuteAdditions()


# Prevents the Python output window from closing until the enter key is pressed
print(line)
input("Press enter to exit.")