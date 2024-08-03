from itertools import permutations 

def p(x):
    if x==1:
        return 0
    if x==2:
        return 1
    for a in range(2, int(x**0.5)+1):
        if x%a==0:
            return 0
    return 1

def lex(str):
    numlist=[]
    perm = sorted(''.join(chars) for chars in permutations(str)) 
    for x in perm: 
        numlist.append(int(x))
    numlist.sort()
    numlist.reverse()
    return numlist
          
str1=''
for m in range(7, 0, -1):
    str1+=str(m)
list1=lex(str1)
print(list1)
for pp in list1:
    if p(pp)==1:
        print(pp)
        break

    
              
