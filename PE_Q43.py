from itertools import permutations 

def lex(str):
    numlist=[]
    perm = sorted(''.join(chars) for chars in permutations(str)) 
    for x in perm: 
        numlist.append(int(x))
    numlist.sort()
    numlist.reverse()
    return numlist

def Diff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

numlist=Diff(lex('123456789'), lex('0123456789'))
total=0
for x in numlist:
    x=str(x)
    if int(x[7:10])%17==0:
        if int(x[6:9])%13==0:
            if int(x[5:8])%11==0:
                if int(x[4:7])%7==0:
                    if int(x[3:6])%5==0:
                        if int(x[2:5])%3==0:
                            if int(x[1:4])%2==0:
                                total+=int(x)

print(total)
        
