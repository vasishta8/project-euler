def p(x):
    if x==1:
        return 1
    elif x==2:
        return 0
    for n in range(2, int(x**0.5)+1):
        if x%n==0:
            return 1
    return 0

def pNext(x):
    x+=1
    while p(x)==1:
        x+=1
    return x

def cyc(x):
    px=len(str(x))
    jst=[]
    if '0' in str(x):
        return 0
    for count in range(px):
        if x not in jst:
            jst.append(int(x))
        x=str(x)
        x=x[1:px]+x[0]
        x=int(x)
    for a in jst:
        if p(a)==1:
            return 0
    return jst[0]

total=0
x=2
cyclist=[]
while x<1000000:
    if cyc(x)!=0 and cyc(x) not in cyclist:
        cyclist.append(cyc(x))
    x=pNext(x)

print(cyclist)
print()
print(len(cyclist))

        

