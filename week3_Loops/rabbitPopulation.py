adult = 0
child = 3
baby = 65
k = 3

for month in range(1, 13):
    new_baby = k * adult
    new_child = baby
    new_adult = adult + child

    adult, child, baby = new_adult, new_child, new_baby

    print(f"Month {month} : {baby} baby, {child} child, {adult} adult")