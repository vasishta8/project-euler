def hcf(a,b):
    c=a%b
    while c!=0:
        a=b
        b=c
        c=a%b
    return b

nmrList=[]
dmrList=[]
for a in range(10,100):
    for b in range(10,100):
        alist=[]
        blist=[]
        if '0' not in str(a) and '0' not in str(b):
            for x in str(a):
                if x in str(b):
                    if a<b:
                        alist=list(str(a))
                        blist=list(str(b))
                        alist.remove(x)
                        blist.remove(x)
                        num1=int(a)/int(b)
                        astr=''
                        bstr=''
                        for p in alist:
                            astr+=p
                        for q in blist:
                            bstr+=q
                        num2=int(astr)/int(bstr)
                        if num1==num2:
                            nmrList.append(int(a))
                            dmrList.append(int(b))

nmrProd=1
dmrProd=1
for a in nmrList:
    nmrProd*=a
for b in dmrList:
    dmrProd*=b

print(dmrProd//hcf(dmrProd,nmrProd))
