# Problem 3.9: Valid Class

number_girls = 7
number_boys = 50

total_students = number_girls + number_boys

#  difference = abs(number_girls - number_boys)   <--- Can be solved easier like that but we have not been taught that yet.

if number_girls > number_boys:
    difference = number_girls - number_boys
else:
    difference = number_boys - number_girls

if total_students > 30:
    status = ("Class is too large")
elif total_students < 10:
    status = ("Class is too small")
elif difference > 3 and (number_boys > number_girls):
    status = ("Too many boys")
elif difference > 3 and (number_girls > number_boys):
    status = ("Too many girls")
elif total_students >= 10 and total_students <= 30 and difference <= 3:
    status = ("Class is ok")
else:
    status = ("Multiple errors")

print("The class with", total_students, "students is:", status)