def fac(x):
    facSum=0
    for a in range(1,x//2+1):
        if x%a==0:
            facSum+=a
    if facSum>x:
        return x
    else:
        return 0
def sig(x):
    newlst=[]
    for a in range(1,x+1):
        newlst.append(a)
    return newlst
abunList=[]
for num in range(1,28123):
    if fac(num)!=0:
        abunList.append(fac(num))

numlst=sig(28123)
heylst=[]
total=0
for j in abunList:
    for w in abunList:
        if j+w<=28123:
            heylst.append(j+w)

def Diff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

total=0
x1=Diff(numlst, heylst)
for pppp in x1:
    total+=pppp
print(total)
        
