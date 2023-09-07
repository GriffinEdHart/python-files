# List of Scores - Griffin Hart - CSD110
# The following program will create a list of 10 integers between 1-10 (not requesting user input)
# Then it will find the lowest score, print it, then remove it from the list.
# The program will then find the highest score, print it, and remove it from the list as well
# Finally, the program will print the average of the remaining scores.

import random

def main():
    compScores = [] # define a list
    for i in range (0, 10): # fill list using random numbers
        score = random.randint(1,10)
        compScores.append(score)

    lowest = min(compScores)
    highest = max(compScores)
    print(f'The first lowest score is {lowest} located at position {compScores.index(lowest)}.')
    print(f'The highest score is {highest} located at position {compScores.index(highest)}') # prints the first highest and lowest scores
    compScores.remove(highest)
    compScores.remove(lowest) # removes the aforementioned scores from the list.

    total = 0.0
    for value in compScores:
        total += value
    compAverage = format((total / len(compScores)), ',.1f')
    print(f'The effective score is {compAverage}.') # Averages the remaining scores and outputs.

main()