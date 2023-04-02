# Coded by Amber Caravalho for the University of Arizona Global Campus
# CPT 200: Fundamentals of Programming Languages//Dr. Amr Elchouemi
# Week 3 - Discussion


# Imports the system and name fields from the OS module
from os import system, name


def clearScreen():
    # Runs the clear screen command for Windows systems
    if name == "nt":
        system("cls")

    # Runs the clear screen command for Mac and Linux system
    else:
        system("clear")


# Prints some sample text
print("\nHey there, this text is just here to take up some space!")


# Allows the user to clear the screen at their leisure
input("Press enter to clear the screen...")


# Calls the main clear screen function
clearScreen()


# Prevents the Python output window from closing until the enter key is pressed
input("Screen cleared, press enter to exit window.")