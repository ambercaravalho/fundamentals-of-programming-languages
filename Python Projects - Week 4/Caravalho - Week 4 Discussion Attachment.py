# Coded by Amber Caravalho for the University of Arizona Global Campus
# CPT 200: Fundamentals of Programming Languages//Dr. Amr Elchouemi
# Week 4 - Discussion


def optionOne():
    print("You chose option 1!\n")


def optionTwo():
    print("You chose option 2!\n")


def optionThree():
    print("You chose option 3!\n")


def doMore():
    # Asks the user to choose what they want to do next
    doMoreUserSelection = str(input("Type a number between 1 and 3: "))

    # Checks if the user input is a number
    if doMoreUserSelection.isnumeric() == True:
        doMoreUserSelection = int(doMoreUserSelection)

        if doMoreUserSelection in (1,2,3):
            # If the user typed 1, optionOne is called
            while doMoreUserSelection == 1:
                optionOne()
                doMore()

            # If the user typed 2, optionTwo is called
            while doMoreUserSelection == 2:
                optionTwo()
                doMore()

            # If the user typed 3, optionThree is called
            while doMoreUserSelection == 3:
                optionThree()
                doMore()
            
        else:
            # Prompts the user to type a valid number
            print("Non-valid input, please type a number between 1 and 3")

            # Calls the doMore function to request user input again
            doMore()
        
    else:
        # Prompts the user to type a valid number
        print("Non-valid input, please type a number between 1 and 3")

        # Calls the doMore function to request user input again
        doMore()


# Runs the main function
doMore()