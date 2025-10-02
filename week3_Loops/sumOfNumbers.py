for n in (5, 10, 15, 33, 42, ):
    currentSum = 0
    for element in range(1, n + 1):
        currentSum = currentSum + element
    print(f"The sum of natural numbers up to {n} is {currentSum}")
