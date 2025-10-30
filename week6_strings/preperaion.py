bm_string = "batmand"
print(bm_string[0])
print(bm_string[3])
print(bm_string[0:3])
print(bm_string[3:])
print(bm_string[::2])
print(bm_string[::-1])

s1 = "DTU"
year = 1829
s = s1 + " " + "is founded in " + str(year)
print(s)
print(len(s))

check1 = 'Maja' == 'Maja'
check2 = 'Maja' == 'maja'
check3 = 'Maja' == 'Maja '
check4 = 'Maja' == "Maja"

print(check1, check2, check3, check4)

my_string = "I am a student at DTU"
my_character = my_string[0]
my_substring = my_string[6:14]

check = my_character + my_substring
print(check)