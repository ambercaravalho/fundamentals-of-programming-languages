# Coded by Amber Caravalho for the University of Arizona Global Campus
# CPT 200: Fundamentals of Programming Languages//Dr. Amr Elchouemi
# Week 1 - Interactive Assignment

# Requests user input, then stores it as a string variable to annual_sales
annual_sales = input("Total Sale: $")

# Converts annual_sales to a float variable
annual_sales = float(annual_sales)

# Calculates 19% of annual_sales and stores it as profit_amount
profit_amount = annual_sales * 0.19

# Rounds profit_amount to 2 digits
profit_amount = (round(profit_amount,2))

# Prints formatted profit to screen
print(f"Profit Amount: ${profit_amount}")