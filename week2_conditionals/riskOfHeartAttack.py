# Problem 3.10: Risk of Heart Attack

age = 45
weight = 80
is_smoker = False

if age < 18:
    if weight < 60:
        high_risk = False
    elif weight >= 60:
        high_risk = True
elif age >= 18 and age <= 30:
    high_risk = False
elif age > 30 and is_smoker == False:
    high_risk = False
elif age > 30 and is_smoker == True:
    high_risk = True

print("Age", age, "weight", weight, "smoker", is_smoker, "high risk", high_risk)