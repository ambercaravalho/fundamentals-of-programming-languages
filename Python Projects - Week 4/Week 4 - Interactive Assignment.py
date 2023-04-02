# Coded by Amber Caravalho for the University of Arizona Global Campus
# CPT 200: Fundamentals of Programming Languages//Dr. Amr Elchouemi
# Week 4 - Interactive Assignment


# Creates the list and variables required for data storage later
numbers = []
entryCounter = 1
line = "---------------------------------------------------"


# Prints the intro to the screen
print(line)
print("Please enter a series of 20 numbers below:")


def requestUserInput():
    # Makes entryCounter a global variable so it can be accessed by this function
    global entryCounter

    # Only requests 20 user inputs
    while entryCounter != 21:
        # Requests user input, then stores them in the list created earlier
        tempNumberStorage = str(input(f"{entryCounter}: "))

        # Checks if the user input is a number
        if tempNumberStorage.isnumeric() == True:
            # Converts the string into an integer
            tempNumberStorage = int(tempNumberStorage)

            # Appends the integer user input to the numbers dictionary
            numbers.append(tempNumberStorage)

            # Advances the dictionary key value each time the script is run
            entryCounter = entryCounter + 1

        else:
            print("Non-Valid Input, please enter positive whole numbers only.")

            requestUserInput()


# Runs the function to ask for user input
requestUserInput()


def dataManipulation():
    # Displays the lowest number out of the user input
    print(f"\nThe lowest number in the list is: {min(numbers)}")

    # Displays the highest number out of the user input
    print(f"The highest number in the list is: {max(numbers)}")

    # Displays the sum of all numbers
    print(f"The sum of the numbers in the list is: {sum(numbers)}")


# Runs the function to display the user input
dataManipulation()


# Asks the user what they want to do next
print(line)
input("Press enter to close...")