def p(x):
    if x==1:
        return 0
    if x==2:
        return 1
    for q in range(2, int(x**0.5)+1):
        if x%q==0:
            return 0
    return 1

def pNext(x):
    x+=1
    while p(x)==0:
        x+=1
    return x

def fact(x):
    n=2
    check=x%n
    count=0
    while n<=x//2:
        if x%n==0:
            count+=1
        n=pNext(n)
    return count-4


templst=[]
for n in range(100000, 200000):
    templst.append(fact(n))

for x in range(4307):
    hoo=templst[x:x+4]
    if hoo==[0,0,0,0]:
        print(x+100000)
        break
    


    

