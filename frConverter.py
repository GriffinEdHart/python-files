# Griffin Hart - 02.06.2023 - Assignment 4, Program 1
# The following program will implement a function: frConverter()
# This function will convert the Fahrenheit temperature (as a parameter)
# To Reaumur, then returns the result to the user.


# The following function is primary for the program. This will ask the user for a temperature in Fahrenheit.
# Following the input(), the function will print the number the user inputted, then send it as a parameter
# to the function frConverter(). Finally, the function will print the converted temperature.
def main(): 
    fTemp = float(input('Enter a temperature in Fahrenheit: '))
    print('You inputted the temperature: ', fTemp, 'degrees, Fahrenheit.')
    rTemp = frConverter(fTemp) # Defines fTemp as the parameter to be used in called function.
    print('Converted, that temperature is equivalent to:', format(rTemp, ',.2f'), 'degrees, Reamur')

# This function will input the parameter inputted by the user into a formula to convert to Reamur (who in the world uses this?)
def frConverter(F):
    finalTemp = (F - 32) * (4/9)
    return finalTemp # When returning a variable, the number defined inside will take the place of the function where it was called.

main() # Starts the program, calls the defined program main().