#Write a functionaverage that takes a list of numbers as input and returns the average of the numbers in the list. Test it with the list from the previous exercise for n=4.

testList = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]


def average(numbers):
    return sum(numbers) / len(numbers)

print(average(testList))

