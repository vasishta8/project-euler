def p(x):
    if x==1:
        return 0
    elif x==2:
        return 1
    for n in range(2, int(x**0.5)+1):
        if x%n==0:
            return 0
    return 1

def pNext(x):
    x+=1
    while p(x)==0:
        x+=1
    return x

def trunct(x):
    n=x
    lst=[x]
    for a in range(len(str(x))-1):
        x=str(x)
        x=x[1:len(str(x))]
        lst.append(int(x))

    for b in range(len(str(n))-1, 0, -1):
        n=str(n)
        n=n[0:b]
        lst.append(int(n))

    lst.sort()
    lst.reverse()
    a1=lst[0]
    for pp in lst:
        if p(pp)==0:
            return [0,0]
    return [a1,1]

total=0
n=11
count=0
while count<2:
    ch=trunct(n)
    total+=ch[0]
    count+=ch[1]
    n=pNext(n)
    print(ch[0])
print(total)
    
        

        
