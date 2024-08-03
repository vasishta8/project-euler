
def q_solve(a,b,c):
    if (b**2)-(4*a*c) < 0:
        return 0.5
    return ((-b+(((b**2)-(4*a*c))**0.5))/(2*a))

"""
def limits(x,y):
    lower = (x//100)*100
    upper = lower+100
    a = para_list[y][0]
    b = para_list[y][1]
    c1 = lower
    c2 = upper
    return (q_solve(a,b,c1), q_solve(a,b,c2))

print(limits(100,100))
for tri in range(45,141):
    trivalue = (tri*(tri+1)//2)
    squ_limits = limits(trivalue,1)
    print(squ_limits)
    for squ in range(squ_limits[0], squ_limits[1]):
        print(squ)
        squvalue = (squ**2)
        squ_limits = limits(squvalue,2)
        for pen in range(squ_limits[0], squ_limits[1]):
            penvalue = (squ*(3*squ-1)//2)
            pen_limits = limits(squvalue,3)
            for heks in range(pen_limits[0], pen_limits[1]):
                hekvalue = (pen*(2*pen))-1
                hek_limits = limits(penvalue,3)
                for hep in range(hek_limits[0], hek_limits[1]):
                    hepvalue = (hek*(5*hek-3)//2)
                    hep_limits = limits(hekvalue,3)
                    for okt in range(hep_limits[0], hep_limits[1]):
                        print(okt)
                        oktvalue = (okt*(3*okt-2))
                        if trivalue//100 == oktvalue % 100:
                            print(tri+squ+pen+hek+hep+okt)

    
"""
def ddd(lst):
    nd = []
    for item in lst:
        if item not in nd:
            nd.append(item)
    return nd

def com(a,b):
    count=0
    fin=[]
    for item in a:
        if item in b:
            count+=1
        else:
            fin.append(item)
    for item in b:
        if item not in a:
            fin.append(item)
    return (count,fin)

tlist = []
slist = []
plist = []
helist = []
hlist = []
olist = []
for i in range(1000,10000):
    if i//100 == i%100:
        continue
    if q_solve(3,-2,-i) == int(q_solve(3,-2,-i)):
        olist.append(i)
    elif q_solve(5,-3,-2*i) == int(q_solve(5,-3,-2*i)):
        hlist.append(i)
    elif q_solve(2,-1,-i) == int(q_solve(2,-1,-i)):
        helist.append(i)
    elif q_solve(3,-1,-2*i) == int(q_solve(3,-1,-2*i)):
        plist.append(i)
    elif q_solve(1,0,-i) == int(q_solve(1,0,-i)):
        slist.append(i)
    elif q_solve(1,1,-2*i) == int(q_solve(1,1,-2*i)):
        tlist.append(i)

for item5 in slist:
    for item2 in hlist:
        for item3 in helist:
            for item4 in plist:
                for item in olist:
                        if com([item//100,item2//100,item3//100,item4//100,item5//100],[item%100,item2%100,item3%100,item4%100,item5%100])[0] == 4 and len(com([item//100,item2//100,item3//100,item4//100,item5//100],[item%100,item2%100,item3%100,item4%100,item5%100])[1]) == 2:
                            d = com([item//100,item2//100,item3//100,item4//100,item5//100],[item%100,item2%100,item3%100,item4%100,item5%100])[1][0]
                            c = com([item//100,item2//100,item3//100,item4//100,item5//100],[item%100,item2%100,item3%100,item4%100,item5%100])[1][1]
                            if (c*100+d) in tlist:
                                temp = [c*100+d,item5,item4,item3,item2,item]
                                temp1 = []
                                temp2 = []
                                for item in temp:
                                    temp1.append(item//100)
                                    temp2.append(item%100)
                                placeholder = []
                                temp3 = temp1[0]
                                for i in range(6):
                                    temp3 = temp1[temp2.index(temp3)]
                                    if temp2.index(temp3) in placeholder:
                                        break
                                    placeholder.append(temp2.index(temp3))
                                    if i==5 and temp3 == temp1[0]:
                                        print(sum(temp), temp)
                                        exit()

