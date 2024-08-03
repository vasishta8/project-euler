def f(x, a):
    sum = 0
    b = a
    while (a < x):
        sum =sum + a
        a = a + b
    return sum

print (f(1000, 3) + f(1000, 5) - f(1000, 15))


print('\007')
