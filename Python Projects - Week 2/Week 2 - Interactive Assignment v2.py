# Coded by Amber Caravalho for the University of Arizona Global Campus
# CPT 200: Fundamentals of Programming Languages//Dr. Amr Elchouemi
# Week 2 - Interactive Assignment v2

primaryColors = ['red', 'yellow', 'blue']
secondaryColors = ['green', 'orange', 'purple']


def mix():
	color1 = input('Please type a primary color (red, yellow, or blue) and press enter: ')
	color2 = input('Please type another primary color and press enter: ')

	if color1.lower() in primaryColors and color2.lower() in primaryColors:
		if color1.lower() == color2.lower():
			return color1.lower()
		n = primaryColors.index(color1.lower())
		m = primaryColors.index(color2.lower())
		return secondaryColors[(n + m) % 3]

	return 'One of the chosen colors is not primary. Please select from red, yellow, or blue.'


print(mix())

response = input('Type anything and press enter to try again. Otherwise, just press enter to quit: ')

while response:
	print(mix())
	response = input('Type anything and press enter to try again. Otherwise, just press enter to quit: ')