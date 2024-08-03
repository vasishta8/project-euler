def hcf(a, b):
    if b>=a:
        g=b
        b=a
        a=g
    c=a%b
    while(c!=0):
        e=b
        b=a%e
        a=e
        c=a%b
    return b

def tot(x):
    to=1
    for a in range(2,x):
        if hcf(x,a)==1:
            to+=1
    return n/to

def p(x):
    if x==1:
        return 0
    elif x==2:
        return 1
    for n in range(2, int(x**0.5)+1):
        if x%n==0:
            return 0
        else:
            pass
    return 1

def next(gg):
    a=gg+1
    while p(a)==0:
        a+=1
    return a

gr=0
n=2
pp=2
while(n<=1000000):
    if tot(n)>=gr:
        gr=tot(n)
        ans=n
    pp=next(pp)
    n*=pp
print(ans)

print(tot(354294))