from math import log

def sod(x):
    total = 0
    for i in str(x):
        total += int(i)
    return total

def dps():
    lst = []
    p=1
    while True:
        for i in range(2,9*(p+1)):
            for j in range(int(log(10**p,i)),int(log(10**(p+1),i))):
                if sod(i**j)==i and i**j>9:
                    lst.append(i**j)
        p+=1
        if len(lst)>30:
            return sorted(lst)

lst1 = dps()
print(lst1[29])