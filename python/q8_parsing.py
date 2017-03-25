# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

with open('football.csv') as csvfile:
    next(csvfile, None)
    readCSV = csv.reader(csvfile, delimiter=',')
    team = "x"
    goal_difference = "None"
    for row in readCSV:
        currentteam = row[0]
        row5 = row[5]
        row6 = row[6]
        goals = int(row5)
        goals_allowed = int(row6)
        difference = goals - goals_allowed
        if goal_difference is "None":
            team = currentteam
            goal_difference = difference
        elif goal_difference < difference:
            team = currentteam
            goal_difference = difference
        else: continue
    print (currentteam)