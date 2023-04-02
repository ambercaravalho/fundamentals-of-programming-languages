# Coded by Amber Caravalho for the University of Arizona Global Campus
# CPT 200: Fundamentals of Programming Languages//Dr. Amr Elchouemi
# Week 2 - Interactive Assignment v1

# Creates two string list objects comprised of primary and secondary color values
colorsPrimary = ['red', 'blue', 'yellow']
colorsSecondary = ['purple', 'orange', 'green']


continueChoice = 'y'


# When called upon, prints the mixed secondary color to the screen (red only) or displays an error
def colorRed(x):
    if x == colorsPrimary[1]:
        print("\nYour mixed secondary color is", colorsSecondary[0], ".")

    if x == colorsPrimary[2]:
        print("\nYour mixed secondary color is", colorsSecondary[1], ".")

    # Displays an error if you type in the same color twice
    if x == "red":
        print("\nERROR - You chose two of the same color.")

    # Displays an error if you typed in anything but a primary color
    if x not in colorsPrimary:
        print("\nERROR - Choose a primary color.")


# Prints the mixed secondary color to the screen (blue only) or displays an error
def colorBlue(x):
    if x == colorsPrimary[0]:
        print("\nYour mixed secondary color is", colorsSecondary[0])

    if x == "yellow":
        print("\nYour mixed secondary color is", colorsSecondary[2])

    # Displays an error if you type in the same color twice
    if x == "blue":
        print("\nERROR - You chose two of the same color.")

    # Displays an error if you typed in anything but a primary color
    if x not in colorsPrimary:
        print("\nERROR - Choose a primary color.")


# Prints the mixed secondary color to the screen (yellow only) or displays an error
def colorYellow(x):
    if x == "red":
        print("orange")


    if x == "blue":
        print("green")

    # Displays an error if you type in the same color twice
    if x == "yellow":
        print("\nERROR - You chose two of the same color.")

    # Displays an error if you typed in anything but a primary color
    if x not in colorsPrimary:
        print("\nERROR - Choose a primary color.")


# Main function: takes two user inputs, then prints their combination to the screen
def colorMix():
        # Requests user input, then saves it to a variable and makes it all lowercase
        colorChoice1 = input("Enter your first color (Red/Blue/Yellow): ").lower()
        colorChoice2 = input("Enter your second color (Red/Blue/Yellow): ").lower()

        # Runs the "colorRed" function if the user enters red first
        if colorChoice1 == colorsPrimary[0]:
            colorRed(colorChoice2)

        # Runs the "colorBlue" function if the user enters blue first
        if colorChoice1 == colorsPrimary[1]:
            colorBlue(colorChoice2) 

        # Runs the "colorYellow" function if the user enters yellow first
        if colorChoice1 == colorsPrimary[2]:
            colorYellow(colorChoice2)

        # Prints an error if the user does not enter a valid primary color
        if colorChoice1 not in colorsPrimary:
            print("\nERROR- Please choose primary colors (Red, Blue, Yellow)")


# Loops the progam if wanted
while continueChoice == "y":
    colorMix()
    continueChoice = input("\nWould you like to continue (y/n): ")


# exit statement
print("\nOkay BYE!\n")