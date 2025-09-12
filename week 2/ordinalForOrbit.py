digit = 5

if digit == 1:
    ordinal = "1st"
elif digit == 2:
    ordinal = "2nd"
elif digit == 3:
    ordinal = "3rd"
else:
    ordinal = str(digit) + "th"

print(ordinal)