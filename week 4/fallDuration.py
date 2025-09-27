#The distance traveled by an object falling from rest is given by the formula
#s = 1/2 * g * t^2
#Where s is the distance traveled (in meters), t is the duration of the fall (in seconds), and g is the gravitationalacceleration due to gravity (approximately 9.81 m/s^2).
#For height a height of 100 meters, calculate the fall duration. Choose four additional heights of your own and calculate the fall duration for each.

def fall_duration(height):
    g = 9.81
    duration = (2 * height / g) ** 0.5
    return duration

print(fall_duration(100))
print(fall_duration(50))
print(fall_duration(150))
print(fall_duration(200))
print(fall_duration(300))