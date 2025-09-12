looks_like_beaver = True
has_beak = True

if looks_like_beaver == True and has_beak == True:
    animal = "Platypus"
elif looks_like_beaver == True and has_beak == False:
    animal = "Beaver"
elif looks_like_beaver == False and has_beak == True:
    animal = "Duck"
else:
    animal = "Fish"

print(animal)
