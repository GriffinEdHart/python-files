"""
The following program is for personal use, to calculate how much each roommate owes for rent.
"""
utilities = float(input("Enter the utilities charges for the month: "))

griffinRent = float(950.00 + 32.50 + 25.00) + (utilities / 3)
anaRent = float(959.50 + 50) + (utilities / 3)
linaRent = float(909.50 + 32.50 + 25.00) + (utilities / 3)

print("Griffin's rent is:", format(griffinRent, ',.2f'))
print("Ana's rent is:", format(anaRent, ',.2f'))
print("Lina's rent is:", format(linaRent, ',.2f'))
