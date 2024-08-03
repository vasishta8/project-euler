def rev(x):
    x=str(x)
    x=x[::-1]
    return int(x)

def pal(x):
    x=str(x)
    if x==x[::-1]:
        return 0
    else:
        return 1

total=0
for m in range(1,10000):
    count=0
    n=m
    while(count<50):
        n=n+rev(n)
        if pal(n)==0:
            total+=1
            count=50
        else:
            count+=1

print(9999-total)