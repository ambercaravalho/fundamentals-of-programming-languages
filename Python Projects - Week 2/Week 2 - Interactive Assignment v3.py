# Coded by Amber Caravalho for the University of Arizona Global Campus
# CPT 200: Fundamentals of Programming Languages//Dr. Amr Elchouemi
# Week 2 - Interactive Assignment v3


# Creates two string list objects comprised of primary and secondary color values
primaryColors = ['red', 'yellow', 'blue']
secondaryColors = ['orange', 'purple', 'green']


# Decorative line to be shown at the beginning and end of the program
line = "---------------------------------------------------"


# Assigns user input to a variable, then makes it lowercase
print(line)
colorChoice1 = input("\nEnter your first color (Red/Yellow/Blue): ").lower()
colorChoice2 = input("Enter your second color (Red/Yellow/Blue): ").lower()


# Ensures that both user inputs are primary colors
if colorChoice1 in primaryColors and colorChoice2 in primaryColors:
    
    # Locates user input within the list above, then assigns a number to it
    colorChoiceNumber1 = primaryColors.index(colorChoice1)
    colorChoiceNumber2 = primaryColors.index(colorChoice2)

    # If both user inputs are the same, that value is printed to the screen
    if colorChoice1 == colorChoice2:
	    print(f"\nYour color is still {colorChoice1}, you just have twice as much of it now.\n")
    
    # Checks if the user inputed colors mix to make orange
    elif colorChoiceNumber1 + colorChoiceNumber2 == 1:
        print("\nYour mixed secondary color is:", secondaryColors[0].capitalize(), "\n")

    # Checks if the user inputed colors mix to make purple
    elif colorChoiceNumber1 + colorChoiceNumber2 == 2:
        print("\nYour mixed secondary color is:", secondaryColors[1].capitalize(), "\n")

    # Checks if the user inputed colors mix to make green
    elif colorChoiceNumber1 + colorChoiceNumber2 == 3:
        print("\nYour mixed secondary color is:", secondaryColors[2].capitalize(), "\n")
  
else: 
    print("\nOne of the chosen colors is not primary! Please select from Red, Yellow, or Blue.\n")


# Prevents the Python output window from closing until the enter key is pressed
print(line)
input("Press enter to exit.")