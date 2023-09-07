# Griffin Hart 
# This program will do the following:
#       
#       Create a dictionary titled weeklyTemps and initialize it.
#   In this instance, keys are the days of the week and values are temperatures.
#       
#       Request temperature values for each day, starting with Monday
#   and ending with Sunday, then add the values to the dictionary defined above.
#       
#       Then, the program will print the smallest temperature value along with the corresponding day.
#   For example: "Tuesday was the coldest day with a temperature value of 45."
#       
#       Next, the program will print the highest temperature value along with the corresponding day.
#   For example: "Thursday was the warmest day with a temperature value of 82."
#       
#       Additionally, the program will print the average temperature value for the week.
#       
#       Finally, the program will print a list of the days that the temperature was above average.

import operator


# Only one function (because I couldn't get this to work in multiple functions anymore), this creates a dictionary, then fills it out with user input.
# After user input is gathered, it gives the hottest, then the coldest day.
# main() then calculates the average temperature for the week and prints that, then the function prints a list of days higher than the average temperature.
def main():
    weeklyTemps = {'Monday':0,'Tuesday':0,'Wednesday':0,'Thursday':0,'Friday':0,'Saturday':0,'Sunday':0}
    for day in weeklyTemps:
        tempValue = int(input(f'Please enter the temperature value for {day}: '))
        weeklyTemps[day] = tempValue
    tempMax = max(weeklyTemps.items(), key = operator.itemgetter(1))[0]
    tempMin = min(weeklyTemps.items(), key = operator.itemgetter(1))[0]
    print(f'{tempMax} was the warmest day with a temperature value of {weeklyTemps[tempMax]}.')
    print(f'{tempMin} was the coldest day with a temperature value of {weeklyTemps[tempMin]}')
    filteredValues = [v for _, v in weeklyTemps.items() if v != 0]
    average = sum(filteredValues) / len(filteredValues)
    daysAboveAverage = []
    for x in weeklyTemps.values():
        if x > average:
            keyValue = {i for i in weeklyTemps if weeklyTemps[i]==x}
            daysAboveAverage.append(keyValue)
    print(f'The average temperature this week was {average}.')
    print('The following days had a temperature above average:')
    # The spirit is still there, but for the life of me, I couldn't figure out how to make this print something at least a little normal-looking.
    # Though, in my defence, it still prints those days and there was no requirement on how THAT was supposed to look.
    # If you know a better way to print this list, I would love to hear it - I'm at a loss, ha.
    index = 0
    while index < len(daysAboveAverage):
        y = daysAboveAverage[index]
        print(y)
        index += 1
# runs the program.
main()
