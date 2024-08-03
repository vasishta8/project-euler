def cycle(x):
    for a in range(1,x-1):
        if 10**a%x==1:
            return 0
    if (10**(x-1)%x)==1:
        return x
    else:
        return 0

def p(x):
    for a in range(2,int(x**0.5)+1):
        if x%a==0:
            return 1
    return 0

def prev(x):
    x-=1
    while p(x)==1:
        x-=1
    return x

num=999
while True:
    if cycle(num)==num:
        break
    num=prev(num)

print(num)
