def p(x):
    if x==1:
        return 0
    elif x==2:
        return 1
    for n in range(2, int(x**0.5)+1):
        if x%n==0:
            return 0
    return 1

def next(x):
    x=x+1
    while(p(x)==0):
        x+=1
    return x

n=600851475143
x=2
list1=[]
while(n>1):
    while(n%x!=0):
        x=next(x)
    list1.append(x)
    n//=x
print(max(list1))
