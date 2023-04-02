# Coded by Amber Caravalho for the University of Arizona Global Campus
# CPT 200: Fundamentals of Programming Languages//Dr. Amr Elchouemi
# Week 5 - Interactive Assignment 2


# Establishes the functions required to gather the file path for import and export functions
from tkinter import *
from tkinter.filedialog import askopenfilename


# Creates the dictionary and variables required for data storage later
masterEmployeeData = {}
firstRun1 = "y"
firstRun2 = "y"
entryCounter = 1
userSelection = 0
line = "---------------------------------------------------"


def addNewEmployee():
    # Makes global variables so they can be accessed by this function
    global entryCounter

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


def viewAllEmployees():
    # Runs if no data exists within the system
    if entryCounter - 1 == 0:
        print("No employee data has been entered into the system.")
    
    # Runs if data exists within the system already
    else:
        # Sets the allEmployeesCountdown variable to the number of employees in the system
        allEmployeesCountdown = entryCounter - 1
        
        while allEmployeesCountdown != 0:
            # Formats and centers the employee's name
            print('\n{:-^50}'.format(f' {masterEmployeeData[f"{allEmployeesCountdown}name"]} '))
                
            # Prints the remaining employee data to the screen
            print(f"SSN: {masterEmployeeData[f'{allEmployeesCountdown}ssn']}")
            print(f"Phone: {masterEmployeeData[f'{allEmployeesCountdown}phone']}")
            print(f"Email: {masterEmployeeData[f'{allEmployeesCountdown}email']}")
            print(f"Salary: ${masterEmployeeData[f'{allEmployeesCountdown}salary']}")
            print(line)

            # Advances the allEmployeesCountdown variable each time the script is run
            allEmployeesCountdown = allEmployeesCountdown - 1


def searchEmployeeBySSN():
    # Makes global variables so they can be accessed by this function
    global firstRun1
    global lookup
    global masterEmployeeData
    global lookupSSN

    # Runs if no data exists within the system
    if entryCounter - 1 == 0:
        print("No employee data has been entered into the system.")

    # Runs if data exists within the system already
    else:
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

            # Calls the searchEmployeeBySSN function to request user input again
            searchEmployeeBySSN()

        if lookupSSN in masterEmployeeData:         
            # Removes all letters from the dictionary key
            lookupSSN = lookupSSN.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyz'})
            
            # Formats and centers the employee's name, then prints it to the screen
            print('\n{:-^50}'.format(f' {masterEmployeeData[f"{lookupSSN}name"]} '))
            
            # Prints the remain employee data to the screen
            print(f"SSN: {masterEmployeeData[f'{lookupSSN}ssn']}")
            print(f"Phone: {masterEmployeeData[f'{lookupSSN}phone']}")
            print(f"Email: {masterEmployeeData[f'{lookupSSN}email']}")
            print(f"Salary: ${masterEmployeeData[f'{lookupSSN}salary']}")
            print(line)

            # Forces the user selection menu to appear again
            userSelectionMenu()
                
        else:
            # Prompts the user to type a valid number
            lookup = str(input("Non-valid input, type an employee's Social Security number (Ex. 289391029): "))

            # Calls the searchEmployeeBySSN function to request user input again
            searchEmployeeBySSN()


def editEmployeeInformation():
    # Makes global variables so they can be accessed by this function
    global firstRun1
    global lookup
    global masterEmployeeData
    global lookupSSN
    global entryCounter

    # Runs if no data exists within the system
    if entryCounter - 1 == 0:
        print("No employee data has been entered into the system.")

    # Runs if data exists within the system already
    else:
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

            # Calls the searchEmployeeBySSN function to request user input again
            editEmployeeInformation()

        if lookupSSN in masterEmployeeData:         
            # Removes all letters from the dictionary key
            lookupSSN = lookupSSN.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyz'})
            
            # Saves the current entryCounter value to another variable
            entryCounterOrig = entryCounter

            # Ensures the correct entry is edited
            entryCounter = int(lookupSSN)

            # Calls the addNewEmployee function to edit the entry
            addNewEmployee()

            # Resets the entryCounter value to what it was before editing the entry
            entryCounter = entryCounterOrig

            # Forces the user selection menu to appear again
            userSelectionMenu()

        else:
            # Prompts the user to type a valid number
            lookup = str(input("Non-valid input, type an employee's Social Security number (Ex. 289391029): "))

            # Calls the editEmployeeInformation function to request user input again
            editEmployeeInformation()


def importEmployeeInformation():
    # Makes global variables so they can be accessed by this function
    global entryCounter

    # Opens the file selection dialog box on your platform
    Tk().withdraw()
    print("Choose an 'Employee Management System Exported Information File' from the window...")
    employeeInformationFilePath = askopenfilename()

    if "txt" in employeeInformationFilePath:
        # Opens the employee information file
        employeeInformationFile = open(f"{employeeInformationFilePath}", "r")

        # Imports the employee information file to a list
        employeeInformationFile = employeeInformationFile.read().splitlines()
        employeeInformationFileLines = len(employeeInformationFile)
        employeeInformationFileLineNumber = 1

        if "--- Employee Management System Exported Information File ---" in employeeInformationFile[0]:
            # Runs until there are no more employee entries to import
            while employeeInformationFileLines != 1:
                masterEmployeeData[f"{entryCounter}name"] = employeeInformationFile[employeeInformationFileLineNumber]
                employeeInformationFileLineNumber = employeeInformationFileLineNumber + 1

                masterEmployeeData[f"{entryCounter}ssn"] = employeeInformationFile[employeeInformationFileLineNumber]
                employeeInformationFileLineNumber = employeeInformationFileLineNumber + 1

                masterEmployeeData[f"{entryCounter}phone"] = employeeInformationFile[employeeInformationFileLineNumber]
                employeeInformationFileLineNumber = employeeInformationFileLineNumber + 1

                masterEmployeeData[f"{entryCounter}email"] = employeeInformationFile[employeeInformationFileLineNumber]
                employeeInformationFileLineNumber = employeeInformationFileLineNumber + 1

                masterEmployeeData[f"{entryCounter}salary"] = employeeInformationFile[employeeInformationFileLineNumber]
                employeeInformationFileLineNumber = employeeInformationFileLineNumber + 1

                # Advances the loop to the next employee entry in the information file
                employeeInformationFileLines = employeeInformationFileLines - 5

                # Advances the masterEmployeeData dictionary key value each time the script is run
                entryCounter = entryCounter + 1

            print("\nThe employee information file was successfully imported!")

        else:
            print("\nThe employee information file failed to import.\nThe selected document was exported by this application.")

    else:
        print("\nThe employee information file failed to import.\nThe selected document was not a text file.")


def exportEmployeeInformation():
    # Runs if no data exists within the system
    if entryCounter - 1 == 0:
        print("No employee data has been entered into the system.")
    
    # Runs if data exists within the system already
    else:
        # Opens the file selection dialog box on your platform
        Tk().withdraw()
        print("Create or choose a text file from the window...")
        employeeInformationFilePath = askopenfilename()

        if "txt" in employeeInformationFilePath:
            # Opens the employee information file in read mode
            employeeInformationFile = open(f"{employeeInformationFilePath}", "r")
            employeeInformationFile = employeeInformationFile.read().splitlines()

            # Checks if the file has been exported to in the past
            if "--- Employee Management System Exported Information File ---" not in employeeInformationFile:
                employeeInformationFile = open(f"{employeeInformationFilePath}", "a")
                employeeInformationFile.write("--- Employee Management System Exported Information File ---")
                
            # Opens/creates the employee information file in append mode
            employeeInformationFile = open(f"{employeeInformationFilePath}", "a")

            # Sets the allEmployeesCountdown variable to the number of employees in the system
            allEmployeesCountdown = entryCounter - 1

            # Appends data to the employee information file until all entries have been appended
            while allEmployeesCountdown != 0:
                employeeInformationFile.write(f'\n{masterEmployeeData[f"{entryCounter - 1}name"]}')
                employeeInformationFile.write(f'\n{masterEmployeeData[f"{entryCounter - 1}ssn"]}')
                employeeInformationFile.write(f'\n{masterEmployeeData[f"{entryCounter - 1}phone"]}')
                employeeInformationFile.write(f'\n{masterEmployeeData[f"{entryCounter - 1}email"]}')
                employeeInformationFile.write(f'\n{masterEmployeeData[f"{entryCounter - 1}salary"]}')

                # Advances the allEmployeesCountdown variable each time the script is run
                allEmployeesCountdown = allEmployeesCountdown - 1

            print("\nThe employee information file was successfully exported!")

        else:
            print("\nThe employee information file failed to export.\nThe selected document was not a text file.")


def userSelectionMenu():
    # Makes firstRun and userSelection global variables so they can be accessed by this function
    global firstRun1
    global firstRun2
    global userSelection
    global entryCounter
    
    while firstRun2 == "y":
        # Formats and centers the banner
        print('\n{:-^51}'.format(" Employee Management System "))

        # If this is the first entry, then the wording is changed
        if entryCounter - 1 == 1:
            print('{: ^50}'.format("There is (1) employee in the system."))

        # If this is not the first entry, then the wording is changed
        else:
            print('{: ^50}'.format(f"There are ({entryCounter - 1}) employees in the system."))
        
        # Asks the user to choose what they want to do next
        print(f"{line}\n1. Add new employee\n2. View all employees\n3. Search employee by SSN\n4. Edit employee information\n5. Import employees’ information from a text file\n6. Export employees’ information to a text file\n7. Exit the application")
        userSelection = str(input(f"{line}\nPlease enter your option number: "))

        firstRun2 = "n"

    if userSelection.isnumeric() == True:
        userSelection = int(userSelection)
        firstRun1 = "y"
        firstRun2 = "y"

        if userSelection in (1,2,3,4,5,6,7):
            # If the user typed 1, addNewEmployee is called
            while userSelection == 1:
                addNewEmployee()
                userSelectionMenu()

            # If the user typed 2, viewAllEmployees is called
            while userSelection == 2:
                viewAllEmployees()
                userSelectionMenu()

            # If the user typed 3, searchEmployeeBySSN is called
            while userSelection == 3:
                searchEmployeeBySSN()
                userSelectionMenu()

            # If the user typed 4, editEmployeeInformation is called
            while userSelection == 4:
                editEmployeeInformation()
                userSelectionMenu()
            
            # If the user typed 5, importEmployeeInformation is called
            while userSelection == 5:
                importEmployeeInformation()
                userSelectionMenu()

            # If the user typed 6, exportEmployeeInformation is called
            while userSelection == 6:
                exportEmployeeInformation()
                userSelectionMenu()

            # If the user typed 7, the application quits
            if userSelection == 7:
                quit()
            
        else:
            # Prompts the user to type a valid number
            userSelection = str(input("Non-valid option selected, type a number between 1 and 7: "))

            # Calls the userSelectionMenu function to request user input again
            userSelectionMenu()
        
    else:
        # Prompts the user to type a valid number
        userSelection = str(input("Non-valid option selected, type a number between 1 and 7: "))

        # Calls the userSelectionMenu function to request user input again
        userSelectionMenu()


# Asks the user what they want to do next
userSelectionMenu()
print(line)