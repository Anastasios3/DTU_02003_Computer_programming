# Bring back five candy wrappers, and you get one candy for free!
# How many candies can you end up eating?

wrappers = 0
candies = 1509
eaten = 0

print("candies:", candies, "wrappers:", wrappers, "eaten:", eaten)

candies = candies - 1
wrappers = wrappers + 1
eaten = eaten + 1

while candies > 0:
    candies = candies - 1
    wrappers = wrappers + 1
    eaten = eaten + 1
    if wrappers >= 5:
        candies = candies + 1
        wrappers = wrappers - 5
    print("candies:", candies, "wrappers:", wrappers, "eaten:", eaten)
