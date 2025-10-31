# Write a function that takes a filename and a surname as input and returns the percentage of people with that surname in the file.
#The expected output for a few of surnames is below.

import os



filename = 'week8_files/weeksFiles/efternavne.csv'

with open(filename) as f:
    print(f.read()) 


print(os.getcwd())