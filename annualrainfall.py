# Annual Rainfall - Dictionaries - Griffin Hart

import operator

def main():
    monthlyRainfall = {}
    totalRainfall = 0
    for i in range (0, 12):
        monthValue = input("Enter the month's name: ")
        rainfallAmount = float(input(f'Enter the rainfall for {monthValue}: '))
        monthlyRainfall[monthValue] = rainfallAmount
        totalRainfall += rainfallAmount
    rainMax = max(monthlyRainfall.items(), key = operator.itemgetter(1)) [0]
    rainMin = min(monthlyRainfall.items(), key = operator.itemgetter(1)) [0]
    filteredValues = [v for _, v in monthlyRainfall.items() if v != 0]
    average = format((totalRainfall / len(filteredValues)), ',.2f')
    
    print(f'The total rainfall for this year was {totalRainfall}')
    print(f'The average monthly rainfall was {average}.')
    print(f'The month with the highest amount of rainfall was {rainMax} with a rainfall value of {monthlyRainfall[rainMax]}')
    print(f'The month with the lowest amount of rainfall was {rainMin} with a rainfall value of {monthlyRainfall[rainMin]}')

main()