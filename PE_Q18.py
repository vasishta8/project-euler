strNum = "75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23 "
checkList=[]
x=0
while x<360:
    if x%3==2:
        x+=1
        continue
    temp=''
    while x%3!=2:
        temp+=strNum[x]
        x+=1
    checkList.append(int(temp))
def tri(x):
    summ=0
    while x>0:
        summ+=x
        x-=1
    return summ


alist=[]
blist=[]
clist=[]
dlist=[]
elist=[]
flist=[]
glist=[]
hlist=[]
ilist=[]
jlist=[]
klist=[]
llist=[]
mlist=[]
nlist=[]

max=0
for a in range(tri(1),tri(1)+2):
    alist.append(checkList[a])
for b in range(tri(2),3+tri(2)):
    blist.append(checkList[b])
for c in range(tri(3),4+tri(3)):
    clist.append(checkList[c])
for d in range(tri(4),5+tri(4)):
    dlist.append(checkList[d])
for e in range(tri(5),tri(5)+6):
    elist.append(checkList[e])
for f in range(tri(6),tri(6)+7):
    flist.append(checkList[f])
for g in range(tri(7),tri(7)+8):
    glist.append(checkList[g])
for h in range(tri(8),tri(8)+9):
    hlist.append(checkList[h])
for i in range(tri(9),tri(9)+10):
    ilist.append(checkList[i])
for j in range(tri(10),tri(10)+11):
    jlist.append(checkList[j])
for k in range(tri(11),tri(11)+12):
    klist.append(checkList[k])
for l in range(tri(12),tri(12)+13):
    llist.append(checkList[l])
for m in range(tri(13),tri(13)+14):
    mlist.append(checkList[m])
for n in range(tri(14),tri(14)+15):
    nlist.append(checkList[n])                                                 
max=0
for a in range(0,2):
    for b in range(a,a+2):
        for c in range(b,b+2):
            for d in range(c,c+2):
                for e in range(d,d+2):
                    for f in range(e,e+2):
                        for g in range(f,f+2):
                            for h in range(g,g+2):
                                for i in range(h,h+2):
                                    for j in range(i,i+2):
                                        for k in range(j,j+2):
                                            for l in range(k,k+2):
                                                for m in range(l,l+2):
                                                    for n in range(m,m+2):
                                                        summm=75+alist[a]+blist[b]+clist[c]+dlist[d]+elist[e]+flist[f]+glist[g]+hlist[h]+ilist[i]+jlist[j]+klist[k]+llist[l]+mlist[m]+nlist[n]
                                                        if summm>=max:
                                                            max=summm
                    

print(max)
                                                
