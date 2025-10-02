#It was claude solving it, i have a brain fart right now

height = 10

for row in range(1, height + 1):

    spaces_needed = height - row
    for space in range(spaces_needed):
        print(" ", end="")

    stars_needed = 2 * row - 1
    for star in range(stars_needed):
        print("*", end="")
    
    print()