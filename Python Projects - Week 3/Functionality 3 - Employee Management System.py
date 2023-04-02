# Coded by Amber Caravalho for the University of Arizona Global Campus
# CPT 200: Fundamentals of Programming Languages//Dr. Amr Elchouemi
# Functionality 3 - Employee Management System


# Creates the dictionary and variables required for data storage later
masterEmployeeData = {}
entryCounter = 1
firstRun1 = "y"
firstRun2 = "y"
doMoreUserSelection = 0


# Prints the line and welcome statement
line = "---------------------------------------------------"
print(line)
print ("Welcome to the Employee Management System!")


def requestUserInput():
    # Makes entryCounter and firstRun global variables so they can be accessed by this function
    global entryCounter
    global firstRun1
    global firstRun2

    # Resets the firstRun variables to "y"
    firstRun1 = "y"
    firstRun2 = "y"

    # Prints the current employee's number to the screen
    print(f"\nPlease enter the information for employee {entryCounter} below:")

    # Requests user input, then stores them in the list created earlier
    masterEmployeeData[entryCounter] = ([input("Employee's Name: "), 
    input("Employee's Social Security Number: "), input("Employee's Phone Number: "), 
    input("Employee's Email Address: "), input("Employee's Salary: $")])

    # Advances the masterEmployeeData dictionary key value each time the script is run
    entryCounter = entryCounter + 1


def lookupEmployee():    
    # Makes firstRun and lookup global variables so they can be accessed by this function
    global firstRun1
    global firstRun2
    global lookup

    # Resets the firstRun2 variable to "y"
    firstRun2 = "y"

    while firstRun1 == "y":
        # Asks the user which employee they want to search for
        lookup = str(input("\nType a number to look up an employee: "))

        # Ensures that this question only display the first time the application is run
        firstRun1 = "n"

    # Makes sure the user input is a number, then converts it to an integer
    if lookup.isnumeric() == True:
        lookup = int(lookup)

        if lookup in masterEmployeeData:
            # Converts the user input list to a string, then prints it to the screen
            print(f"\n{line}")
            print(", ".join(masterEmployeeData[lookup]))
            print(line)
            
        else:
            # Prompts the user to type a valid number
            lookup = str(input("Non-valid input, please type an employee's number: "))

            # Calls the lookupEmployee function to request user input again
            lookupEmployee()
        
    else:
        # Prompts the user to type a valid number
        lookup = str(input("Non-valid input, please type a number: "))

        # Calls the lookupEmployee function to request user input again
        lookupEmployee()


# Runs the function for the first run
requestUserInput()


def doMore():
    # Makes firstRun and doMoreUserSelection global variables so they can be accessed by this function
    global firstRun1
    global firstRun2
    global doMoreUserSelection
    global entryCounter
    
    while firstRun2 == "y":
        # Asks the user to choose what they want to do next
        print(f"\nThere are ({entryCounter - 1}) employees in the system. What would you like to do next?\nType '1' to add another entry to the system.\nType '2' to look up an employee.\nType '3' to exit the application.")
        doMoreUserSelection = str(input("Type a number between 1 and 3: "))

        firstRun2 = "n"

    if doMoreUserSelection.isnumeric() == True:
        doMoreUserSelection = int(doMoreUserSelection)

        if doMoreUserSelection in (1,2,3):
            # If the user typed 1, requestUserInput is called
            while doMoreUserSelection == 1:
                requestUserInput()
                doMore()

            # If the user typed 2, lookupEmployee is called
            while doMoreUserSelection == 2:
                firstRun1 = "y"
                lookupEmployee()
                doMore()

            # If the user typed 3, the applicaiton quits
            if doMoreUserSelection == 3:
                pass
            
        else:
            # Prompts the user to type a valid number
            doMoreUserSelection = str(input("Non-valid input, please type a number between 1 and 3: "))

            # Calls the doMore function to request user input again
            doMore()
        
    else:
        # Prompts the user to type a valid number
        doMoreUserSelection = str(input("Non-valid input, please type a number between 1 and 3: "))

        # Calls the doMore function to request user input again
        doMore()


# Asks the user what they want to do next
doMore()
print(line)