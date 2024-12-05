import os
os.chdir("C:/Users/Ben/Documents/advent-of-code/day2")

# Safe
#   in ascending or descending order
#   difference between adjacent elements is between 1 and 3

# Split the two columns from text file into 2 lists
reports = []
with open("input.txt", "r") as file:
    for line in file:
        p = line.split()
        reports.append(p)

safe_count = 0
for report in reports:
    for element in reports:
        if
