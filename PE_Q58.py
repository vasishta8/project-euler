def p(x):
    if x==1:
        return 0
    elif x==2:
        return 1
    for n in range(2, int(x**0.5)+1):
        if x%n==0:
            return 0
    return 1

num=1
jump=2
nmr=0
dmr=1
percent=100
jump=2
while percent>=10:
    count=0
    while count<4:
        num+=jump
        dmr+=1
        if p(num)==1:
            nmr+=1
        count+=1
    percent=nmr/dmr*100
    jump+=2
print(jump-1)
    
    
