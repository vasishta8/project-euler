"""
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        for g in range(10):
                            for h in range(10):
                                n = int("1"+str(a)+"2"+str(b)+"3"+str(c)+"4"+str(d)+"5"+str(e)+"6"+str(f)+"7"+str(g)+"8"+str(h)+"9")
                                if (n**0.5)%1 == 0:
                                    print((n*100)**0.5)
                                    exit()

"""
from itertools import product
def catenate(lst):
    s = ""
    for item in lst:
        s+=item
    return int(s)
def weave(list1,list2):
    lijst = []
    i = 0
    while i < len(list2):
        lijst.append(list1[i])
        lijst.append(list2[i]) 
        i += 1
    lijst.append(list1[i])
    return catenate(lijst)
check = [list(x) for x in list(product("0123456789",repeat=8))]
for item in check:
    item2 = weave(list("123456789"),item)
    if int(item2**0.5)==item2**0.5:
        print((item2*100)**0.5)
        exit()
