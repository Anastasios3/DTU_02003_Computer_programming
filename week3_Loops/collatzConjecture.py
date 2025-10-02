n = 34
i = 0

while n != 1:
    i = i + 1
    print(n, end=" -> ")
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    print(n)
    print("Done in", i, "steps")