def p(x):
    if x==1:
        return 0
    elif x==2:
        return 1
    for n in range(2, int(x**0.5)+1):
        if x%n==0:
            return 0
    return 1

bList=[]
aList=[]
lenList=[]
for b in range(2,1001):
    if p(b)==1:
        bList.append(b)

for b in bList:
    maxA=0
    maxLength=0
    for a in range((-1-b),1001):
        length=0
        n=0
        result=n**2+a*n+b
        if result<1:
            pass
        else:
            while p(result)==1:
                length+=1
                n+=1
                result=n**2+a*n+b
                if result<1:
                    break
            if n>=maxLength:
                maxLength=n
                maxA=a
    aList.append(maxA)
    lenList.append(maxLength)

index=lenList.index(max(lenList))
print((aList[index])*(bList[index]))

        
            
    

