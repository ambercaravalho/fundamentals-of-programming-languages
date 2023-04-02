NumList = []
for j in range(1, 10 + 1):
    const = int(input("Enter %d number: " %j))
    NumList.append(const)
print("\n List of all entered numbers: ",NumList)
print("\n Sum of all numbers is equal to: ", sum(NumList))
print("\n Smallest number entered is: ", min(NumList))
print("\n Largest number entered is: ", max(NumList))