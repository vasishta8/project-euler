maxx=918273645
maxlist=[1,2,3,4,5,6,7,8,9]
for n in range(2,6):
    num=9//n
    for pp in range(9*(10**(num-1)), 10**num):
        xstr=''
        for a in range(1,n+1):
            nn=a*pp
            xstr+=str(nn)
        if len(xstr)==9:
            list1=[]
            for ab in xstr:
                list1.append(int(ab))
            list1.sort()
            if list1==maxlist and int(xstr)>=maxx:

                maxx=int(xstr)

print(maxx)
        
                
    
