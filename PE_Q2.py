def f(n):
    x = 1
    y = 2
    sum = 2
    while (x < n and y < n):
        x = x + y
        if (x%2==0):
            sum=sum+x
        y = y + x
        if (y%2==0):
            sum=sum+y
    return sum

print (f(4000000))