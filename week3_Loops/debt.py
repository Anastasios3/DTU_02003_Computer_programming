debt = 20000
monthly_payment = 2000
interest_rate = 0.05

total_paid = 0
months = 0

while debt > 0:
    months += 1
    interest = interest_rate * debt
    debt = debt + interest
    
    if debt <= monthly_payment:
        payment_this_month = debt
        debt = 0
    else:
        payment_this_month = monthly_payment
        debt = debt - monthly_payment
    
    total_paid += payment_this_month

print(f"Debt paid after {months} months.")
print(f"Total payment {total_paid:.2f} kr.")