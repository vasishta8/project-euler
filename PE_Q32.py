ansList=[]
numList=[1,2,3,4,5,6,7,8,9]
for a in range(12,100):
    for b in range(123, 1000):
        haList=[]
        rodList=[]
        c=a*b
        alist=list(str(a))
        blist=list(str(b))
        clist=list(str(c))
        haList=alist+blist+clist
        for x in haList:
            rodList.append(int(x))
        rodList.sort()
        if rodList==numList and c not in ansList:
            ansList.append(c)

for a in range(1,10):
    for b in range(1234, 10000):
        haList=[]
        rodList=[]
        c=a*b
        if len(str(c))==4:
            alist=list(str(a))
            blist=list(str(b))
            clist=list(str(c))
            haList=alist+blist+clist
            for x in haList:
                rodList.append(int(x))
            rodList.sort()
            if rodList==numList and c not in ansList:
                ansList.append(c)

total=0
for p in ansList:
    total+=p

print(total)
            
        
        
