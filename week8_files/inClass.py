# Write a function that takes a filename and a surname as input and returns the percentage of people with that surname in the file.
#The expected output for a few of surnames is below.

import os

filename = 'week8_files/weeksFiles/efternavne.csv'
name = "Brown"
target_num = 0


def surname_percentage(filename, name):
    number = 0
    total = 0
    with open(filename) as f:
        for line in f.readlines():
            line_split = line.split(',')
            name_line = line_split[0]
            if name == name_line:
                target_num = number
            number = int(line_split[1])
            total += number
    print(f"Total number of people: {total}")
    percentage = (target_num / total) * 100
    print(f"Percentage of people with surname {name}: {percentage:.2f}%")

surname_percentage(filename, name)
surname_percentage('week8_files/weeksFiles/efternavne.csv', 'Olsen')
surname_percentage('week8_files/weeksFiles/efternavne.csv', 'Jensen')
#surname_percentage('week8_files/weeksFiles/efternavne.csv', 'Hohoho')
print(os.getcwd())