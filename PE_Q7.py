def p(x):
    if x==1:
        return 0
    elif x==2:
        return 1
    for n in range(2, int(x**0.5)+1):
        if x%n==0:
            return 0
    return 1

n=1
a=3
while(n<=10000):
    n+=p(a)
    a+=2
    

print(a-2)

