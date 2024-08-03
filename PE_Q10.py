def p(x):
    if x==1:
        return 0
    elif x==2:
        return x
    for n in range(2, int(x**0.5)+1):
        if x%n==0:
            return 0
    return x

sum=5
for a in range(6,2000000,6):
    sum+=p(a-1)+p(a+1)
print(sum)