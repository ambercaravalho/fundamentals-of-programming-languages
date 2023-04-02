# Coded by Amber Caravalho for the University of Arizona Global Campus
# CPT 200: Fundamentals of Programming Languages//Dr. Amr Elchouemi
# Functionality 4 - Employee Management System


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
    masterEmployeeData[f"{entryCounter}name"] = input("Employee's Name: ")
    masterEmployeeData[f"{entryCounter}ssn"] = input("Employee's Social Security Number: ")
    masterEmployeeData[f"{entryCounter}phone"] = input("Employee's Phone Number: ")
    masterEmployeeData[f"{entryCounter}email"] = input("Employee's Email Address: ")
    masterEmployeeData[f"{entryCounter}salary"] = input("Employee's Salary: $")

    # Advances the masterEmployeeData dictionary key value each time the script is run
    entryCounter = entryCounter + 1


def lookupSingleEmployeeBySSN():
    # Makes firstRun and lookup global variables so they can be accessed by this function
    global firstRun1
    global firstRun2
    global lookup
    global masterEmployeeData
    global lookupSSN

    # Resets the firstRun2 variable to "y"
    firstRun2 = "y"

    while firstRun1 == "y":
        # Asks the user which employee they want to search for
        lookup = str(input("\nType an employee's Social Security number to look them up: "))

        # Ensures that this question only display the first time the application is run
        firstRun1 = "n"

    # Converts the dictionary's keys and values into their own lists
    masterEmployeeDataKeys = list(masterEmployeeData.keys())
    masterEmployeeDataValues = list(masterEmployeeData.values())

    if lookup in masterEmployeeDataValues:
        # Looks up the key from the dictionary by searching for the value
        lookupSSNValues = masterEmployeeDataValues.index(lookup)
        lookupSSN = masterEmployeeDataKeys[lookupSSNValues]

    else:
        # Prompts the user to type a valid number
        lookup = str(input("Non-valid input, type an employee's Social Security number (Ex. 289391029): "))

        # Calls the lookupSingleEmployeeBySSN function to request user input again
        lookupSingleEmployeeBySSN()

    if lookupSSN in masterEmployeeData:         
        # Removes all letters from the dictionary key
        lookupSSN = lookupSSN.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyz'})
            
        # Formats and centers the employee's name, then prints it to the screen
        employeeNameBanner = "{:-^50}".format(masterEmployeeData[f"{lookupSSN}name"])
        print(f"\n{employeeNameBanner}")
            
        # Prints the remain employee data to the screen
        print(f"SSN: {masterEmployeeData[f'{lookupSSN}ssn']}")
        print(f"Phone: {masterEmployeeData[f'{lookupSSN}phone']}")
        print(f"Email: {masterEmployeeData[f'{lookupSSN}email']}")
        print(f"Salary: ${masterEmployeeData[f'{lookupSSN}salary']}")
        print(line)

        doMore()
            
    else:
        # Prompts the user to type a valid number
        lookup = str(input("Non-valid input, type an employee's Social Security number (Ex. 289391029): "))

        # Calls the lookupSingleEmployeeBySSN function to request user input again
        lookupSingleEmployeeBySSN()


def editEmployeeInformation():
    # Makes firstRun and lookup global variables so they can be accessed by this function
    global firstRun1
    global firstRun2
    global lookup
    global masterEmployeeData
    global lookupSSN
    global entryCounter

    # Resets the firstRun2 variable to "y"
    firstRun2 = "y"

    while firstRun1 == "y":
        # Asks the user which employee they want to search for
        lookup = str(input("\nType an employee's Social Security number to edit their entry: "))

        # Ensures that this question only display the first time the application is run
        firstRun1 = "n"

    # Converts the dictionary's keys and values into their own lists
    masterEmployeeDataKeys = list(masterEmployeeData.keys())
    masterEmployeeDataValues = list(masterEmployeeData.values())

    if lookup in masterEmployeeDataValues:
        # Looks up the key from the dictionary by searching for the value
        lookupSSNValues = masterEmployeeDataValues.index(lookup)
        lookupSSN = masterEmployeeDataKeys[lookupSSNValues]

    else:
        # Prompts the user to type a valid number
        lookup = str(input("Non-valid input, type an employee's Social Security number (Ex. 289391029): "))

        # Calls the lookupSingleEmployeeBySSN function to request user input again
        editEmployeeInformation()

    if lookupSSN in masterEmployeeData:         
        # Removes all letters from the dictionary key
        lookupSSN = lookupSSN.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyz'})
        
        # Saves the current entryCounter value to another variable
        entryCounterOrig = entryCounter

        # Ensures the correct entry is edited
        entryCounter = int(lookupSSN)

        # Calls the requestUserInput function to edit the entry
        requestUserInput()

        # Resets the entryCounter value to what it was before editing the entry
        entryCounter = entryCounterOrig

        doMore()

    else:
        # Prompts the user to type a valid number
        lookup = str(input("Non-valid input, type an employee's Social Security number (Ex. 289391029): "))

        # Calls the editEmployeeInformation function to request user input again
        editEmployeeInformation()


def viewAllEmployees():
    # Makes firstRun a global variable so it can be accessed by this function
    global firstRun2
    
    # Resets the firstRun2 variable to "y"
    firstRun2 = "y"

    # Sets the allEmployeesCountdown variable to the number of employees in the system
    allEmployeesCountdown = entryCounter - 1
    
    while allEmployeesCountdown != 0:
        # Formats and centers the employee's name, then prints it to the screen
        employeeNameBanner = '{:-^50}'.format(masterEmployeeData[f"{allEmployeesCountdown}name"])
        print (" "); print (employeeNameBanner)
            
        # Prints the remain employee data to the screen
        print(f"SSN: {masterEmployeeData[f'{allEmployeesCountdown}ssn']}")
        print(f"Phone: {masterEmployeeData[f'{allEmployeesCountdown}phone']}")
        print(f"Email: {masterEmployeeData[f'{allEmployeesCountdown}email']}")
        print(f"Salary: ${masterEmployeeData[f'{allEmployeesCountdown}salary']}")
        print(line)

        # Advances the allEmployeesCountdown variable each time the script is run
        allEmployeesCountdown = allEmployeesCountdown - 1


# Runs the function for the first run
requestUserInput()


def doMore():
    # Makes firstRun and doMoreUserSelection global variables so they can be accessed by this function
    global firstRun1
    global firstRun2
    global doMoreUserSelection
    global entryCounter
    
    while firstRun2 == "y":
        # If this is the first entry, then the wording is changed
        if entryCounter - 1 == 1:
            print(f"\nThere is (1) employee in the system. What would you like to do next?")

        # If this is not the first entry, then the wording is changed
        else:
            print(f"\nThere are ({entryCounter - 1}) employees in the system. What would you like to do next?")
        
        # Asks the user to choose what they want to do next
        print("Type '1' to add another employee entry to the system.\nType '2' to edit an employee entry.\nType '3' to look up an employee entry.\nType '4' to view all employee entries.\nType '5' to exit the application.")
        doMoreUserSelection = str(input("Type a number between 1 and 5: "))

        firstRun2 = "n"

    if doMoreUserSelection.isnumeric() == True:
        doMoreUserSelection = int(doMoreUserSelection)

        if doMoreUserSelection in (1,2,3,4,5):
            # If the user typed 1, requestUserInput is called
            while doMoreUserSelection == 1:
                firstRun1 = "y"
                requestUserInput()
                doMore()

            # If the user typed 2, editEmployeeInformation is called
            while doMoreUserSelection == 2:
                firstRun1 = "y"
                editEmployeeInformation()
                doMore()
            
            # If the user typed 3, lookupSingleEmployeeBySSN is called
            while doMoreUserSelection == 3:
                firstRun1 = "y"
                lookupSingleEmployeeBySSN()
                doMore()

            # If the user typed 4, viewAllEmployees is called
            while doMoreUserSelection == 4:
                firstRun1 = "y"
                viewAllEmployees()
                doMore()

            # If the user typed 5, the applicaiton quits
            if doMoreUserSelection == 5:
                quit()
            
        else:
            # Prompts the user to type a valid number
            doMoreUserSelection = str(input("Non-valid input, please type a number between 1 and 5: "))

            # Calls the doMore function to request user input again
            doMore()
        
    else:
        # Prompts the user to type a valid number
        doMoreUserSelection = str(input("Non-valid input, please type a number between 1 and 5: "))

        # Calls the doMore function to request user input again
        doMore()


# Asks the user what they want to do next
doMore()
print(line)