# Problem 3.11: Triangle Type

x = 2
y = 2
z = 3

if x==0 or y==0 or z==0:
    is_triangle = False
else:
    if x > y and x > z:
        largest = x
    elif y > z and y > x:
        largest = y
    else:
        largest = z

    if largest == x:
        if y + z > x:
            is_triangle = True
        else:
            is_triangle = False
    elif largest == y:
        if x + z > y:
            is_triangle = True
        else:
            is_triangle = False
    elif largest == z:
        if x + y > z:
            is_triangle = True
        else:
            is_triangle = False

    if is_triangle == False:
        triangle_type = "Not a triangle"
    else:

        if x == y == z:
            triangle_type = "Equilateral"
        elif x == y or y == z or x == z:
            triangle_type = "Isosceles"
        else:
            triangle_type = "Scalene"

if is_triangle == False:
    print("Not a triangle")
else:
    print("The triangle with sides", x, ",", y, ",", z, "is:", triangle_type)