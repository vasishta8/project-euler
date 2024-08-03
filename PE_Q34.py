def fac(x):
    prod=1
    while x>0:
        prod*=x
        x-=1
    return prod

def facadd(x):
    x=str(x)
    totall=0
    for abc in x:
        totall+=fac(int(abc))
    return totall

total=0
for pp in range(10, 1000000):
    if facadd(pp)==pp:
        total+=pp

print(total)
