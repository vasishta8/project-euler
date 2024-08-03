def lcm(a, b):
    x=a
    y=b
    if a>=b:
        pass
    else:
        a1=b
        b=a
        a=a1    
    c=a%b
    if c==0:
        return x*y/b
    while(c!=0):
        a1=b
        b1=c
        c=a1%b1
    return x*y/b1

prod=1
n=1
while(n<=20):
    prod=lcm(prod,n)
    n+=1

print(prod)