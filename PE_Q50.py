def p(x):
    if x==1:
        return 0
    if x==2:
        return 1
    for a in range(2,int(x**0.5)+1):
        if x%a==0:
            return 0
    return 1

def pnext(x):
    x=x+1
    while p(x)!=1:
        x+=1
    return x

plst=[]
a=2
totall=0
while totall<1000000:
    plst.append(a)
    totall+=a
    a=pnext(a)
z=plst.pop()
totall-=z
plst.reverse()

while p(totall)==0:
    totall-=plst.pop()

print(totall)
#72169