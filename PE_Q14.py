def collatz(x):
    count = 0
    x = x * 2
    while (x % 2 == 0):
        x //= 2
        count += 1
        while (x % 2 == 1):
            if x == 1:
                break
            x = 3 * x + 1
            count += 1
    return count

maximum = 0
for a in range (1, 1000000):
    if collatz(a) >= maximum:
        maximum = collatz(a)
        final = a
print (final)