def ps(x):
    b=(1+(1+4*3*2*x)**0.5)/6
    if b==b//1:
        return x
    else:
        return 0

def pj(x):
    b=((1+(1+4*3*2*x)**0.5))//6
    return int(b)

def p(x):
    return x*(3*x-1)//2

x=2
high=0
while True:
    for y in range(1,x):
        add=p(x)+p(y)
        sub=p(x)-p(y)
        if ps(add)==add and ps(sub)==sub:
            high=sub
    if high==0:
        x+=1
    else:
        print(high)
        break
    
