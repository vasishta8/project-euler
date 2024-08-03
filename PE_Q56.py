def d(x):
    sum=0
    x=str(x)
    for a in x:
        sum+=int(a)
    return sum

max=0
for a in range(2,100):
    for b in range(1, 100):
        if a%10!=0:
            if d(a**b)>=max:
                max=d(a**b)

print(max)
            
