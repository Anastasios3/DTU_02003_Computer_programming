# Problem 3.8: Body Temperature

temperature = 36.5

if temperature <= 36.0 and temperature >= 30.0:
    state = ("Hypothermia")
elif temperature > 36.0 and temperature <= 37.5:
    state = ("Normal")
elif temperature > 37.5 and temperature <= 40.0:
    state = ("Hyperthermia")
elif temperature > 40.0:
    state = ("Hyperpyrexia")
else:
    state = ("Input Error")

print("The temperature", temperature, "is", state)