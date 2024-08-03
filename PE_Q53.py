def fac(x):
    prod=1
    while x>0:
        prod*=x
        x-=1
    return prod

def comb(a,b):
    x=fac(a)
    y=fac(b)*fac(a-b)
    return x//y

total=0
for a in range(1,101):
    for b in range(a//2+1):
        if comb(a,b)>1000000:
            if b==a-b:
                total-=1
            total+=2

print(total)
