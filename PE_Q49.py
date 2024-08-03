def p(x):
    if x==1:
        return 0
    if x==2:
        return 1
    for n in range(2, int(x**0.5)+1):
        if x%n==0:
            return 0
    return 1

def srt(x):
    list1=list(str(x))
    list1.sort()
    strr=''
    for a in list1:
        strr+=a
    return strr

primeList = []
for a in range(1000, 10000):
    if p(a) == 1:
        primeList.append(a)

for x in primeList:
    for y in range((9999-x)//2, 1, -1):
        u=x+y
        v=x+y+y
        if u in primeList and v in primeList:
            if srt(x)==srt(u) and srt(u)==srt(v) and x!=1487:
                print(x*10**8+u*10**4+v)
                break
    break
                

#ans is 296962999629






