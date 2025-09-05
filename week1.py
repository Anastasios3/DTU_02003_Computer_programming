hours = 23
minutes = 59
delay = 2

arrivalHours = hours
arrivalMinutes = minutes + delay

arrivalHours = arrivalHours + arrivalMinutes // 60

arrivalMinutes = arrivalMinutes % 60

arrivalHours = arrivalHours % 24

print ("The train arrives: ", arrivalMinutes, "after", arrivalHours)
print(arrivalHours, ":", arrivalMinutes)