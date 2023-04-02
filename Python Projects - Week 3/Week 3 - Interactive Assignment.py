# Coded by Amber Caravalho for the University of Arizona Global Campus
# CPT 200: Fundamentals of Programming Languages//Dr. Amr Elchouemi
# Week 3 - Interactive Assignment


# Defines and prints the line
line = "--------------------------------------------"
print(line)


# Ensures the function is set correctly for first run
firstRun = "y"
addAnotherEntry = "y"


def mainFunction():
    def requestUserInput():
        # Ensures that all functions can use this variable
        global userInput
        global firstRun
        
        # Requests a user to input a number greater than one
        userInput = str(input("\nPlease enter a number greater than one to compute: "))

        # Ensures the function is set correctly for first run
        firstRun = "y"

        # If the user did not type a number, this runs
        if userInput.isnumeric() == False:
            # Tells the user that they did not type a number
            print("Invalid Input - Please enter a number!")

            # Runs the function again
            requestUserInput()

        # If a user did type a number, this runs
        else:
            # Converts the user's number into an integer
            userInput = int(userInput)

            if userInput > 1:
                # Do nothing if the user typed a number greater than one
                pass

            else:
                # Tells the user that they did not type a number greater than one
                print("Invalid Input - Please enter a number greater than one!")

                # Runs the function again
                requestUserInput()


    # Initially calls the function for application first run
    requestUserInput()


    def userChoice():
        # Ensures that all functions can use these variables
        global dataSelection
        global userInput

        # Requests a user to input a one or two
        dataSelection = input("Type '1' to see a countdown to zero or type '2' to calculate a factorial: ")

        # If the user did not type a number, this runs
        if dataSelection.isnumeric() == False:
            # Tells the user that they did not type a number
            print("Invalid Input - Please enter a number!")

            # Runs the function again
            userChoice()

        # If a user did type a number, this runs
        else:
            # Converts the user's number into an integer
            dataSelection = int(dataSelection)

            # Runs if the user typed one
            if dataSelection == 1:
                # Displays the first number
                print(f"\nCountdown from {userInput}:")
                
                # Runs while userInput is above 0
                while userInput != 0:
                    # Subtracts one from ther user's input
                    userInput = userInput - 1
                    
                    # Display the countdown
                    print(userInput)

            # Runs if the user typed 2
            elif dataSelection == 2:
                factorial = 1

                # Calculates the factorial by utilizing the power of math
                for i in range(1, userInput + 1):
                    factorial = factorial * i
                
                # Displays the factorial
                print(f"\nYour factorial is: {factorial}")
        
            else:
                # Tells the user that they did not type one or two
                print("Invalid Input - Please enter either '1' or '2'!")

                # Runs the function again
                userChoice()


    # Initially calls the function for application first run
    userChoice()


# Initially calls the function for application first run
mainFunction()


def computeMore():
    # Ensures that all functions can use these variables
    global addAnotherEntry
    global firstRun

    while addAnotherEntry == "y":
        # Asks the user if they want to run the application again
        if firstRun == "y":
            # Asks the user if they want to run the application again
            addAnotherEntry = str(input("\nWould you like to compute another number? (Y/N): ")).lower()

            # Ensures this if loop only runs the first time
            firstRun = "n"

        # Runs if the user typed y
        elif addAnotherEntry == "y":
            # Runs the main function again
            mainFunction()

    while addAnotherEntry != "n":
        # Tells the user that they need to type a y or n
        addAnotherEntry = str(input("Invalid Input - Please type either 'Y' or 'N': ")).lower()

        # Runs the function again        
        computeMore()


# Initially calls the function for application first run
computeMore()


# Prevents the Python output window from closing until the enter key is pressed
print(f"\n{line}")
input("Press enter to exit.")