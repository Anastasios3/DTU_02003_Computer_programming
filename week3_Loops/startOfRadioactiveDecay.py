R = 0.9
amount = 2.5
hours = 45

for hour in range(1, hours + 1):
    amount = amount * R
    print(f"After {hour} hour(s), the amount is: {amount:.4f} grams")
