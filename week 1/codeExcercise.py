a = 10
b = 4
c = 2
d = 6

# Uses standard order: multiplication before division
result1 = (a - d) * (b / c)
# Exponential with fractional power (b/c)
result2 = (a - d) ** (b / c)
# Exponential with b, then divided by c
result3 = (a - d) ** b / c

print(result1)
print(result2)
print(result3)

